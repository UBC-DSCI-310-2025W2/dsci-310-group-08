# Data
**This `data/` folder contains the required data for this project.**
- The [`raw/` folder](raw/) will contain the raw dataset for this project. It will generate locally after running the script `1_download-data.py` **Please do NOT edit the file in this folder**.
- The [`processed/` folder](processed/) contains any processed datasets for this project. However, the processed data is listed in [`.gitignore`](../.gitignore) and is not tracked on GitHub. Instead, it will be generated locally when you run the script `2_process-data.py`.
- If you would like to download the raw data `.csv` file to your local machine, you can run the following command in your terminal:
  
`curl https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2021/2021-06-22/parks.csv`
