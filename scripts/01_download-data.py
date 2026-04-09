# imports
import pandas as pd
import click
from pathlib import Path

@click.command()
# add option to specify input path
@click.option(
    "--input_path",
    required=True,
    type=str
)
# add option to specify output path
@click.option(
    "--output_path",
    required=True,
    type=click.Path()
)

# add option to specify output path for data dictionary
@click.option(
    "--output_path_data_dict",
    required=True,
    type=click.Path()
)

def download_data(input_path, output_path, output_path_data_dict):
    # read in raw data
    data_raw = pd.read_csv(input_path)

    # create path to store raw data
    output_path = Path(output_path)
    data_raw.to_csv(output_path, index=False)

    # create the data dictionary
    data_dict = [
        ["year", "double", "Year of measurement"],
        ["rank", "double", "Yearly rank"],
        ["city", "character", "City Name"],
        ["med_park_size_data", "double", "Median park size acres"],
        ["med_park_size_points", "double", "Median park size in points"],
        ["park_pct_city_data", "character", "Parkland as percentage of city area"],
        ["park_pct_city_points", "double", "Parkland as % of city area points"],
        ["pct_near_park_data", "character", "Percent of residents within a 10 minute walk to park"],
        ["pct_near_park_points", "double", "Percent of residents within a 10 minute walk to park points"],
        ["spend_per_resident_data", "character", "Spending per resident in USD"],
        ["spend_per_resident_points", "double", "Spending per resident in points"],
        ["basketball_data", "double", "Basketball hoops per 10,000 residents"],
        ["basketball_points", "double", "Basketball hoops per 10,000 residents points"],
        ["dogpark_data", "double", "Dog parks per 100,000 residents"],
        ["dogpark_points", "double", "Dog parks per 100,000 residents points"],
        ["playground_data", "double", "Playgrounds per 10,000 residents"],
        ["playground_points", "double", "Playgrounds per 10,000 residents points"],
        ["rec_sr_data", "double", "Recreation and senior centers per 20,000 residents"],
        ["rec_sr_points", "double", "Recreation and senior centers per 20,000 residents points"],
        ["restroom_data", "double", "Restrooms per 10,000 residents"],
        ["restroom_points", "double", "Restrooms per 10,000 residents points"],
        ["splashground_data", "double", "Splashgrounds and splashpads per 100,000 residents"],
        ["splashground_points", "double", "Splashgrounds and splashpads per 100,000 residents points"],
        ["amenities_points", "double", "Amenities points total (ie play areas)"],
        ["total_points", "double", "Total points (varies in denominator per/year)"],
        ["total_pct", "double", "Total points as a percentage"],
        ["city_dup", "character", "City duplicated name"],
        ["park_benches", "double", "Number of park benches"]
        ]
    data_dict = pd.DataFrame(data_dict, columns=["variable", "class", "description"])
    
    # create path to store data dictionary
    output_path_data_dict = Path(output_path_data_dict)
    data_dict.to_csv(output_path_data_dict, index=False)

if __name__ == "__main__":
    download_data()