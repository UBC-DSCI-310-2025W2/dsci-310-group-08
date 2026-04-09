import pandas as pd
import click
import sys
import os

# Import the create_directory and split_dataset functions from parks_pkg_dsci310_08 package
from parks_pkg_dsci310_08.parks import create_directory, split_dataset

@click.command()
@click.option(
    "--data_path",
    required=True,
    type=click.Path(exists=True)
)
@click.option(
    "--splits_path",
    required=True,
    type=click.Path()
)

def split_data(data_path, splits_path):
    data_processed = pd.read_csv(data_path)

    # split data into train and test sets using abstracted function
    X_train, X_test, y_train, y_test = split_dataset(
        data_processed, target_col="rank", test_size=0.2, random_state=73
    )

    # create directory to store the data splits
    splits_path = create_directory(splits_path)

    # save splits to files
    X_train.to_csv(splits_path / "X_train.csv", index=False)
    X_test.to_csv(splits_path / "X_test.csv", index=False)
    y_train.to_csv(splits_path / "y_train.csv", index=False)
    y_test.to_csv(splits_path / "y_test.csv", index=False)


if __name__ == "__main__":
    split_data()