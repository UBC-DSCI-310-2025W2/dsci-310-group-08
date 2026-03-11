import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_validate, RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from scipy.stats import loguniform
from pathlib import Path

# import split datasets
X_train = pd.read_csv("../data/processed/splits/X_train.csv")
y_train = pd.read_csv("../data/processed/splits/y_train.csv")
X_test = pd.read_csv("../data/processed/splits/X_test.csv")
y_test = pd.read_csv("../data/processed/splits/y_test.csv")

# manually recoding the year feature as a category since it did not persist from storing the data as a csv
X_train['year'] = X_train['year'].astype('category')

# isolating different types of features
categorical_features = X_train.select_dtypes(include=["object", "string", "category"]).drop(columns=['city']).columns.tolist()
numerical_features = X_train.select_dtypes(include=['int', 'float']).columns.tolist()
numerical_features.remove('rank_last_time')
drop_features = ['city', 'rank_last_time']

# preprocessor
preprocessor = make_column_transformer(
    (OneHotEncoder(handle_unknown='ignore'), categorical_features),
    (StandardScaler(), numerical_features),
    ("drop", drop_features)
)

# model pipeline
pipe = make_pipeline(preprocessor, Ridge())

# hyperparameter tuning
param_grid = {'ridge__alpha': loguniform(1e-3, 1e3)}

grid_search = RandomizedSearchCV(pipe, param_distributions=param_grid, random_state=123,
                                 n_iter=100, n_jobs=-1, return_train_score=True)
grid_search.fit(X_train, y_train)

# get feature names after preprocessing
feature_names = grid_search.best_estimator_.named_steps['columntransformer'].get_feature_names_out()

# zip into a dataframe
train_coef_df = pd.DataFrame({
    'feature': feature_names,
    'coefficient': grid_search.best_estimator_.named_steps['ridge'].coef_
}).sort_values('coefficient', key=abs, ascending=False)

train_coef_df['feature'] = train_coef_df['feature'].str.replace('onehotencoder__', '').str.replace('standardscaler__', '')

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

# store predictions to be called by script 6 - results
y_preds_df = pd.DataFrame({
    "y_true": y_test.squeeze(),
    "y_pred": y_pred
})

Path("../data/processed/predictions").mkdir(parents=True, exist_ok=True)
y_preds_df.to_csv("../data/processed/predictions/test_predictions.csv", index = False)