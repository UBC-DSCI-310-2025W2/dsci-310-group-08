# imports
import pandas as pd
from pathlib import Path

# read in raw data
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2021/2021-06-22/parks.csv"
data_raw = pd.read_csv(url)

# create path to store raw data
Path("../data/raw").mkdir(parents=True, exist_ok=True)
data_raw.to_csv("../data/raw/parks_raw.csv", index=False)

# verify the script worked
# print(data_raw.head())