# imports
import pandas as pd
import click
from pathlib import Path

@click.command()
# add option to specify input path
@click.option(
    "--input_path",
    default="https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2021/2021-06-22/parks.csv"
)
# add option to specify output path
@click.option(
    "--output_path",
    default="../data/raw/parks_raw.csv"
)

def download_data(input_path, output_path):
    # read in raw data
    data_raw = pd.read_csv(input_path)

    # create path to store raw data
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data_raw.to_csv(output_path, index=False)

if __name__ == "__main__":
    download_data()