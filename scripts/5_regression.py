import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_validate, RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# import split datasets
X_train = pd.read_csv("../data/processed/splits/X_train.csv")
y_train = pd.read_csv("../data/processed/splits/y_train.csv")

# manually recoding the year feature as a category since it did not persist from storing the data as a csv
X_train['year'] = X_train['year'].astype('category')

# isolating different types of features
categorical_features = X_train.select_dtypes(include=["object", "string", "category"]).drop(columns=['city']).columns.tolist()
numerical_features = X_train.select_dtypes(include=['int', 'float']).columns.tolist()
drop_features = ['city']

# preprocessor
preprocessor = make_column_transformer(
    (OneHotEncoder(handle_unknown='ignore'), categorical_features),
    (StandardScaler(), numerical_features),
    ("drop", drop_features)
)

# model pipeline
pipe = make_pipeline(preprocessor, Ridge())