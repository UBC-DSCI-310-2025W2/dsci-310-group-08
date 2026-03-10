import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns

data_processed = pd.read_csv("../data/processed/parks_processed.csv")

# split data into train and test set
X = data_processed.drop(['rank'], axis = 1)
y = data_processed['rank']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8) 

# create the paths for plots
Path("../artifacts").mkdir(parents=True, exist_ok=True)
Path("../artifacts/eda").mkdir(parents=True, exist_ok=True)

# make first plot - frequency of ranks
plt.hist(y_train, bins = 12, edgecolor='black')
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Figure 1: Ordinal Rank vs Value Frequency in the Training Set");
plt.savefig("../artifacts/eda/1_rank_frequency.png")

# second plot - frequency of previous ranks
plt.hist(X_train['rank_last_time'], bins = 12, edgecolor='black', color = 'green')
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Figure 2: Previous Rank Value vs Frequency it Appears in the Training Set");
plt.savefig("../artifacts/eda/2_rank-last-time_frequency.png")

# third plot - boxplot of point-based features
columns_to_plot = ['med_park_size_points', 'park_pct_city_points',
       'pct_near_park_points', 'spend_per_resident_points',
       'basketball_points', 'dogpark_points', 'playground_points',
       'rec_sr_points', 'amenities_points']

sns.boxplot(data=X_train[columns_to_plot])
plt.title("Figure 3: Boxplots of the Point-based Features")
plt.xticks(rotation=45, ha='right')
plt.show()
plt.savefig("../artifacts/eda/3_numerical_boxplots.png")