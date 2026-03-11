import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns

# import split data
X_train = pd.read_csv("../data/processed/splits/X_train.csv")
y_train = pd.read_csv("../data/processed/splits/y_train.csv")

# create the paths for plots
Path("../outputs").mkdir(parents=True, exist_ok=True)
Path("../outputs/eda").mkdir(parents=True, exist_ok=True)

# make first plot - frequency of ranks
plt.hist(y_train, bins = 12, edgecolor='black')
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Figure 1: Ordinal Rank vs Value Frequency in the Training Set");
plt.savefig("../outputs/eda/01_rank_frequency.png")
# clear plot
plt.clf()

# second plot - frequency of previous ranks
plt.hist(X_train['rank_last_time'], bins = 12, edgecolor='black', color = 'green')
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Figure 2: Previous Rank Value vs Frequency it Appears in the Training Set");
plt.savefig("../outputs/eda/02_rank-last-time_frequency.png")
plt.clf()

# third plot - boxplot of point-based features
columns_to_plot = ['med_park_size_points', 'park_pct_city_points',
       'pct_near_park_points', 'spend_per_resident_points',
       'basketball_points', 'dogpark_points', 'playground_points',
       'rec_sr_points', 'amenities_points']

plt.figure(figsize=(10,9))
sns.boxplot(data=X_train[columns_to_plot])
plt.title("Figure 3: Boxplots of the Point-based Features")
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.5, left = 0.2)
plt.savefig("../outputs/eda/03_numerical_boxplots.png", pad_inches=10)