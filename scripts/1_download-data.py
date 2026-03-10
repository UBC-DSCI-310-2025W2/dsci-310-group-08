# imports
import pandas as pd

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2021/2021-06-22/parks.csv"
data_raw = pd.read_csv(url)
data_raw.to_csv("../data/raw/parks_raw.csv", index=False)

# verify the script worked
# print(data_raw.head())