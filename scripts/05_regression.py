import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder
from scipy.stats import loguniform
import click
from pathlib import Path
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.create_directory import create_directory 
from src.get_model_coefficients import get_model_coefficients

@click.command()
@click.option(
    "--splits_path",
    required=True,
    type=click.Path(exists=True)
)
@click.option(
    "--predictions_path",
    required=True,
    type=click.Path()
)

@click.option(
    "--predictions_result_path",
    required=True,
    type=click.Path()
)

def regression(splits_path, predictions_path, predictions_result_path):
    # import split datasets
    splits_path = Path(splits_path)
    X_train = pd.read_csv(splits_path / "X_train.csv")
    y_train = pd.read_csv(splits_path / "y_train.csv")
    X_test = pd.read_csv(splits_path / "X_test.csv")
    y_test = pd.read_csv(splits_path / "y_test.csv")
    
    # manually recoding the year feature as a category since it did not persist from storing the data as a csv
    X_train['year'] = X_train['year'].astype('category')
    X_test['year'] = X_test['year'].astype('category')
    
    # isolating different types of features
    categorical_features = X_train.select_dtypes(include=["object", "string", "category"]).drop(columns=['city']).columns.tolist()
    numerical_features = X_train.select_dtypes(include=['int', 'float']).drop(columns=['rank_last_time']).columns.tolist()
    drop_features = ['city', 'rank_last_time']
    
    # preprocessor
    preprocessor = make_column_transformer(
        (OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ("passthrough", numerical_features),
        ("drop", drop_features)
    )
    
    # model pipeline
    pipe = make_pipeline(preprocessor, Ridge())
    
    # hyperparameter tuning
    param_grid = {'ridge__alpha': loguniform(1e-3, 1e3)}
    
    grid_search = RandomizedSearchCV(
        pipe, param_distributions=param_grid, random_state=73, n_iter=100, n_jobs=-1, return_train_score=True
        )
    grid_search.fit(X_train, y_train)
        
    # new model pipeline using tuned alpha
    final_pipe = make_pipeline(preprocessor, Ridge(alpha=grid_search.best_params_['ridge__alpha']))
    final_pipe.fit(X_train, y_train)
    
    # get feature names after preprocessing
    train_coef_df = get_model_coefficients(final_pipe)
    
    # predict on test data
    y_pred = final_pipe.predict(X_test)
    
    # store predictions to be called by script 6 - results
    y_preds_df = pd.DataFrame({
        "y_true": y_test.squeeze(),
        "y_pred": y_pred
    })

    # create directory for predictions and write predictions to directory
    predictions_path = create_directory(predictions_path)
    
    predictions_result_path = Path(predictions_result_path)
    
    # save best alpha and the corresponding accuracy score from grid search to csv
    pd.DataFrame({
        'best_alpha': [grid_search.best_params_['ridge__alpha']],
        'best_score': [grid_search.best_score_]
        }).to_csv(predictions_result_path / "grid_search_results.csv", index=False)
    
    # save coefficients learned by the model
    train_coef_df.to_csv(predictions_result_path / "model_coef.csv", index=False)
    
    # export processed data to csv in the processed folder
    y_preds_df.to_csv(predictions_path / "test_predictions.csv", index=False)

if __name__ == "__main__":
    regression()