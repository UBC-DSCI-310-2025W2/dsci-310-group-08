import pandas as pd
import pandera.pandas as pa
import numpy as np
import click
from pathlib import Path

# Schema Definition
schema = pa.DataFrameSchema(
    {
        'year': pa.Column(
            pd.CategoricalDtype(),
            pa.Check.isin(['2015', '2016', '2017', '2018', '2019', '2020']),
            nullable=False
            ), 
        'rank': pa.Column(
            int, pa.Check.between(1,98), nullable=False), 
        'rank_last_time': pa.Column(int, pa.Check.gt(0)),
        'state': pa.Column(
            pd.CategoricalDtype(),
            pa.Check.isin(['NM', 'CA', 'AK', 'TX',
                           'VA', 'GA', 'CO', 'MD',
                           'LA', 'ID', 'MA', 'NY', 
                           'AZ', 'NC', 'IL', 'OH', 
                           'IA', 'MI', 'IN', 'NV', 
                           'FL', 'HI', 'NJ', 'MO', 
                           'KY', 'NE', 'WI', 'TN', 
                           'MN', 'OK', 'PA', 'OR', 
                           'WA', 'DC', 'KS']),
            nullable=False
            ), 
        '.*_points': pa.Column(float, nullable=True, regex=True),
    },
    checks=[
        pa.Check(lambda df: ~df.duplicated().any(), error="Duplicate rows found."),
        pa.Check(lambda df: ~(df.isna().all(axis=1)).any(), error="Empty rows found.")

    ]
)

# Data Validation
@click.command()
@click.option("--processed_path", required=True, type=click.Path(exists=True))
@click.option("--output_path", required=True, type=click.Path())
def validate_data(processed_path, output_path):
    parks_processed = pd.read_csv(processed_path, dtype={"year": "category", "state": "category"})
    schema.validate(parks_processed)
    Path(output_path).write_text("Validation passed.")

if __name__ == "__main__":
    validate_data()