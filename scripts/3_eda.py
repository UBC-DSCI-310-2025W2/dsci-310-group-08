import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from pathlib import Path

data_processed = pd.read_csv("../data/processed/parks_processed.csv")

# split data into train and test set
X = data_processed.drop(['rank'], axis = 1)
y = data_processed['rank']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8) 

# create the paths for plots
Path("../artifacts").mkdir(parents=True, exist_ok=True)
Path("../artifacts/eda").mkdir(parents=True, exist_ok=True)

# make first plot
plt.hist(y_train, bins = 12, edgecolor='black')
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Figure 1: Ordinal Rank vs Value Frequency in the Training Set");
plt.savefig("../artifacts/eda/rank_frequency.png")