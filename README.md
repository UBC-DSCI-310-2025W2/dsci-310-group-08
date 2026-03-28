# Predicting Park Access Rankings Across U.S. Cities :national_park:
**DSCI 310 Group 08**\
**Authors**: Shivani Aggarwal, Luna Gulec, Jingyuan Liu, Sarenna Ulman

## About
In this project, we intend to use the Parks dataset to build a ridge regression model to predict a city’s park access ranking in the United States. Using characteristics of each city's park system, demographic information, and population features, such as total park acreage, number of parks, population size, and population density, we aim to determine which factors are most strongly associated with high park access rankings and to build predictive models to accurately predict rankings of cities given those features. 

The dataset contains annual park system data for major U.S. cities up to 2021 and is sourced from the Trust for Public Land’s ParkScore index. The data was obtained from the TidyTuesday repository and can be accessed [here](https://github.com/rfordatascience/tidytuesday/blob/main/data/2021/2021-06-22/readme.md)

By identifying the features that distinguish top-ranked cities, our ridge regression model was able to predict city park system rankings with relatively strong performance with a test $R^2$ of approximately 0.803. The results suggest that measurable park attributes, such as park size, accessibility, and amenities, contribute meaningfully to `ParkScore` rankings. While categorical features like `year` and `state` had a large influence, point-based features including `spend_per_resident_points`, `pct_near_park_points`, and `park_pct_city_points` were associated with better predicted rankings. These findings indicate which aspects of park systems urban planners could prioritize to improve accessibility, equity, and overall park quality.

## Reports
The `.ipynb` notebook report of this project can be found [here](reports/parks_analysis.ipynb).

The `.qmd` Quarto report file can be found [here](reports/parks_analysis.qmd).

The rendered `HTML` report can be found [here](https://ubc-dsci-310-2025w2.github.io/dsci-310-group-08/), and the rendered `PDF` report can be found [here](docs/index.pdf).

## Repository Structure
Before running `make all`, or after running `make clean`:
```
.
├── .github/
│   └── workflows/
│
├── data/
│   ├── README.md
│   ├── raw/
│   │   └── .gitkeep
│   └── processed/
│       └── .gitkeep
│
├── outputs/
│   ├── eda/
│   │   └── .gitkeep
│   └── results/
│       └── .gitkeep
|
├── reports/
│   ├── parks_analysis.ipynb
|   ├── parks_analysis.qmd
|   ├── README.md
│   └── references.bib
│
├── scripts/
│   ├── 01_download-data.py
│   ├── 02_process-data.py
│   ├── 03_split-data.py
│   ├── 04_eda.py
│   ├── 05_regression.py
│   └── 06_results.py
|
├── src/
│   ├── create_directory.py
│   ├── find_measurement_last_time.py
│   ├── get_model_coefficients.py
│   └── split_dataset.py
|
├── tests/
│   ├── test_create_directory.py
│   ├── test_find_measurement_last_time.py
│   ├── test_get_model_coefficients.py
│   └── test_split_dataset.py
|
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docker-compose.yml
├── Dockerfile
├── LICENSE.md
├── Makefile
└── README.md
```
After running `make all`:
```
.
├── .github/
│   └── workflows/
│
├── data/
│   ├── README.md
│   ├── raw/
│   │   ├── .gitkeep
│   │   ├── data_dict.csv
│   │   └── parks_raw.csv
│   └── processed/
│       ├── .gitkeep
│       ├── parks_processed.csv
│       |── predictions/
│       |   └── test_predictions.csv
│       └── splits/
│           ├── X_test.csv
│           ├── X_train.csv
│           ├── y_test.csv
│           └── y_train.csv
│
|── docs/
│   ├── index.html
│   └── index.pdf
│
├── outputs/
│   ├── eda/
│   │   ├── .gitkeep
│   │   ├── 01_rank_frequency.png
│   │   ├── 02_rank-last-time_frequency.png
│   │   ├── 03_rank_rank-last-time_scatter.png
│   │   ├── 04_numerical_boxplots.png
│   │   └── X_train_summary.csv
│   └── results/
│       ├── .gitkeep
│       ├── 05_actual-vs-predicted.png
│       ├── grid_search_results.csv
│       └── model_coef.csv
|
├── reports/
│   ├── parks_analysis.ipynb
|   ├── parks_analysis.qmd
|   ├── README.md
│   └── references.bib
│
├── scripts/
│   ├── 01_download-data.py
│   ├── 02_process-data.py
│   ├── 03_split-data.py
│   ├── 04_eda.py
│   ├── 05_regression.py
│   └── 06_results.py
|
├── src/
│   ├── create_directory.py
│   ├── find_measurement_last_time.py
│   ├── get_model_coefficients.py
│   └── split_dataset.py
|
├── tests/
│   ├── test_create_directory.py
│   ├── test_find_measurement_last_time.py
│   ├── test_get_model_coefficients.py
│   └── test_split_dataset.py
│
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docker-compose.yml
├── Dockerfile
├── LICENSE.md
├── Makefile
└── README.md
```

*To keep the repository lightweight, data files and output files are not tracked on GitHub. While the folder architecture remains visible on GitHub to preserve the project structure via `.gitkeep` files, the actual files will be generated locally as demonstrated above after running `make clean` followed by `make all`.*

## Instructions
**We use a Docker container image to make the computational environment reproducible for this project.**
- You will use Docker to recreate the computational environment for this analysis. For this, you will need a Docker account. You can sign up for a free one [here](https://app.docker.com/accounts/ljy0401).
- After signing up and signing into the Docker Store, go [here](https://docs.docker.com/desktop/setup/install/windows-install/) and click on the “Get Docker Desktop” button on the right-hand side of the screen. Then follow the installation instructions on that screen to install the stable version.

*Please ignore the above two steps if you already have Docker set up.*

- Open `Terminal` on your local machine and navigate to the project's root directory using the `cd` command.
- Make sure your Docker is running.
- Run the following command to start the environment: `docker-compose up --build jupyter`.
- Once the container has launched, users need to navigate to a web browser (i.e., Chrome) and copy the URL `http://localhost:8887/lab` into their web browser to access Jupyter Lab.
- Enter `dsci310_group_08` as the token/password to log into Jupyter Lab.
- Next, in Jupyter Lab, you should be able to see all files and folders in our project repo there.

*We recommend you to use **GNU Make** to automate the project, either to clean up existing outputs and rendered Quarto reports or to render the `.qmd` source file into `PDF` and `HTML` formats or to execute **unit tests** for our **abstracted functions** using `pytest`. You can achieve all of these via simple command-line arguments. Please follow the instructions below:*

- Launch a new Terminal **inside Jupyter Lab** (If you cannot find where to launch a Terminal inside Jupyter Lab, please watch this very short [video](https://www.youtube.com/watch?v=ynMjz1tiq9o)). You should see something like `(base) jovyan@xxxxxxxxxxxx:~/work$` in the terminal.
- To clean up existing outputs and rendered Quarto reports, type `make clean` and press <kbd>ENTER</kbd>. 
- To render the `.qmd` source file into `PDF` and `HTML` formats, type `make all` and press <kbd>ENTER</kbd>. 
- To execute unit tests for the abstracted functions, type `pytest tests/` and press <kbd>ENTER</kbd>, then wait for all tests to be executed.
- Once you are done, press <kbd>CTRL</kbd>+<kbd>C</kbd> in your **local Terminal (outside the Jupyter Lab container)** to close Jupyter Lab.
- Then type `docker-compose down` in the **local Terminal** to stop and clean up the launched container.

## Dependencies
- Python 3.13.11, Jupyter and Python Packages listed in the default scipy notebook base Docker image [here](https://github.com/jupyter/docker-stacks/wiki/x86_64-default-scipy-notebook-0dd81e2dd718).
- [Quarto v1.8.26](https://quarto.org/docs/blog/posts/2025-10-13-1.8-release/).
- [TinyTeX v2026.03.02](https://github.com/rstudio/tinytex-releases/releases)
- [pytest 9.0.2](https://pypi.org/project/pytest/)

## Licenses
This project report is offered under 
the [Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
The code and software provided in this project are offered under the [MIT open source license](https://opensource.org/licenses/MIT). See [the license file](LICENSE.md) for more information. 
