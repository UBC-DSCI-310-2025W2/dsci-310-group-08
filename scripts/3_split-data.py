import pandas as pd
from sklearn.model_selection import train_test_split

data_processed = pd.read_csv("../data/processed/parks_processed.csv")

# split data into train and test set
X = data_processed.drop(['rank'], axis = 1)
y = data_processed['rank']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8) 

# save splits to files
X_train.to_csv("../data/processed/splits/X_train.csv", index=False)
X_test.to_csv("../data/processed/splits/X_test.csv", index=False)
y_train.to_csv("../data/processed/splits/y_train.csv", index=False)
y_test.to_csv("../data/processed/splits/y_test.csv", index=False)