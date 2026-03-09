# imports
import pandas as pd

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2021/2021-06-22/parks.csv"
data_raw = pd.read_csv(url)

# verify the script worked
# print(data_raw.head())