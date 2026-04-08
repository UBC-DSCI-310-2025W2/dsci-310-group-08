import pandas as pd
import matplotlib.pyplot as plt
import click
from pathlib import Path
import seaborn as sns

@click.command()
@click.option(
    "--splits_path",
    required=True,
    type=click.Path(exists=True)
)
@click.option(
    "--outputs_path",
    required=True,
    type=click.Path()
)
@click.option(
    "--fig1_name",
    required=True
)
@click.option(
    "--fig2_name",
    required=True
)
@click.option(
    "--fig3_name",
    required=True
)
@click.option(
    "--fig4_name",
    required=True
)

def eda(splits_path, outputs_path, fig1_name, fig2_name, fig3_name, fig4_name):
    # import split data
    splits_path = Path(splits_path)
    X_train = pd.read_csv(splits_path / "X_train.csv")
    y_train = pd.read_csv(splits_path / "y_train.csv")
    
    # create the paths for plots
    outputs_path = Path(outputs_path)
    
    # make first plot - frequency of ranks
    plt.hist(y_train, bins = 12, edgecolor='black')
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Training Set Ordinal Rank vs Value Frequency")
    plt.savefig(outputs_path / fig1_name)
    # clear plot
    plt.clf()
    
    # second plot - frequency of previous ranks
    plt.hist(X_train['rank_last_time'], bins = 12, edgecolor='black', color = 'green')
    plt.xlabel("Rank")
    plt.ylabel("Frequency")
    plt.title("Training Set Previous Rank Value vs Frequency")
    plt.savefig(outputs_path / fig2_name)
    plt.clf()
    
    # third plot - scatterplot of current and previous ranks
    plt.scatter(X_train['rank_last_time'], y_train['rank'], edgecolor='black',zorder=1)
    plt.grid(True)
    plt.gca().set_axisbelow(True)
    plt.xlabel("Previous Rank")
    plt.ylabel("Current Rank")
    plt.title("Previous Rank vs Current Rank")
    plt.savefig(outputs_path / fig3_name)
    plt.clf()
    
    # fourth plot - boxplot of point-based features
    columns_to_plot = ['med_park_size_points', 'park_pct_city_points',
           'pct_near_park_points', 'spend_per_resident_points',
           'basketball_points', 'dogpark_points', 'playground_points',
           'rec_sr_points', 'amenities_points']
    
    plt.figure(figsize=(10,6))
    sns.boxplot(data=X_train[columns_to_plot])
    plt.xticks(rotation=45, ha='right')
    plt.title("Boxplots of Point-based Features")
    plt.tight_layout()
    plt.savefig(outputs_path / fig4_name)
    
    # training data summary table
    train_summary = X_train.describe()
    train_summary.to_csv(outputs_path / "X_train_summary.csv", index=True)

if __name__ == "__main__":
    eda()