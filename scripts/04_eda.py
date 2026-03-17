import pandas as pd
import matplotlib.pyplot as plt
import click
from pathlib import Path
import seaborn as sns

@click.command()
@click.option(
    "--splits_path",
    # default="../data/processed/splits"
    required=True,
    type=click.Path(exists=True)
)
@click.option(
    "--outputs_path",
    # default="../outputs/eda"
    required=True,
    type=click.Path()
)
@click.option(
    "--fig1_name",
    # default="01_rank_frequency.png"
    required=True
)
@click.option(
    "--fig2_name",
    # default="02_rank-last-time_frequency.png"
    required=True
)
@click.option(
    "--fig3_name",
    # default="03_numerical_boxplots.png"
    required=True
)

def eda(splits_path, outputs_path, fig1_name, fig2_name, fig3_name):
    # import split data
    splits_path = Path(splits_path)
    X_train = pd.read_csv(splits_path / "X_train.csv")
    y_train = pd.read_csv(splits_path / "y_train.csv")
    
    # create the paths for plots
    outputs_path = Path(outputs_path)
    outputs_path.mkdir(parents=True, exist_ok=True)
    
    # make first plot - frequency of ranks
    plt.hist(y_train, bins = 12, edgecolor='black')
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Figure 1: Ordinal Rank vs Value Frequency in the Training Set");
    plt.savefig(outputs_path / fig1_name)
    # clear plot
    plt.clf()
    
    # second plot - frequency of previous ranks
    plt.hist(X_train['rank_last_time'], bins = 12, edgecolor='black', color = 'green')
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Figure 2: Previous Rank Value vs Frequency it Appears in the Training Set");
    plt.savefig(outputs_path / fig2_name)
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
    plt.savefig((outputs_path / fig3_name), pad_inches=10)

if __name__ == "__main__":
    eda()
    