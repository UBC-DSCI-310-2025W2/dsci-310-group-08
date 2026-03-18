# Predicting Park Access Rankings Across U.S. Cities :national_park:
**DSCI 310 Group 08**\
**Authors**: Shivani Aggarwal, Luna Gulec, Jingyuan Liu, Sarenna Ulman

## About
In this project, we intend to use the Parks dataset to build a regression model to predict a city’s park access ranking in the United States. Using characteristics of each city's park system, demographic information, and population features, such as total park acreage, number of parks, population size, and population density, we aim to determine which factors are most strongly associated with high park access rankings and to build predictive models to accurately predict rankings of cities given those features. 

By identifying the features that distinguish top-ranked cities, this model could help city urban planners and policymakers understand why certain parks may be preferred over others and how to improve park accessibility, equity, and overall system performance.

The dataset contains annual park system data for major U.S. cities up to 2021 and is sourced from the Trust for Public Land’s ParkScore index. The data was obtained from the TidyTuesday repository and can be accessed [here](https://github.com/rfordatascience/tidytuesday/blob/main/data/2021/2021-06-22/readme.md)

## Report
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
│       └── splits/
│           └── .gitkeep
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
│   ├── 06_results.py
│   └── 07_clean.py
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
│   │   └── 03_numerical_boxplots.png
│   └── results/
│       ├── .gitkeep
│       └── 04_actual-vs-predicted.png
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
│   ├── 06_results.py
│   └── 07_clean.py
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

*To keep the repository lightweight, processed data and output files are not tracked on GitHub. While the folder architecture remains visible on GitHub to preserve the project structure via `.gitkeep` files, the actual files will be generated locally as demonstrated above after running `make clean` followed by `make all`.*

## Instructions
**We use a Docker container image to make the computational environment reproducible for this project.**\
*Please ignore the first two steps if you already have Docker set up.*
- You will use Docker to recreate the computational environment for this analysis. For this, you will need a Docker account. You can sign up for a free one [here](https://app.docker.com/accounts/ljy0401).
- After signing up and signing into the Docker Store, go [here](https://docs.docker.com/desktop/setup/install/windows-install/) and click on the “Get Docker Desktop” button on the right-hand side of the screen. Then follow the installation instructions on that screen to install the stable version.

*If you want to interactively run our `.ipynb` noyebook, and/or edit any files (i.e., `.md` files, `Makefile`, `Dockerfile`, `.qmd` files, and etc.) in our project repository, you can launch Jupyter Lab by following the instructions below:*

- Open your terminal and navigate to the project's root directory using the `cd` command.
- Make sure your Docker is running.
- Run the following command to start the environment: `docker-compose up --build jupyter`.
- Once the container has launched, users need to navigate to a web browser (i.e., Chrome) and copy the URL `http://localhost:8887/lab` into their web browser to access Jupyter Lab.
- Enter `dsci310_group_08` as the token/password to log into Jupyter Lab.
- Next, in Jupyter Lab, you should be able to see all files and folders in our project repo there.
- Once you are done, <kbd>CTRL</kbd>+<kbd>C</kbd> to stop and clean up the launched container.
- Then type `docker-compose down` in the terminal.

*If you want to use **GNU Make** to automate the project, either to clean up existing outputs and rendered Quarto reports or to render the `.qmd` source file into `PDF` and `HTML` formats, please follow the instructions below:*

- Open your terminal and navigate to the project's root directory using the `cd` command.
- Make sure your Docker is running.
- Run the following command to start the environment: `docker-compose run --rm --build make`.
- Wait for the prompt to appear. You should see something like `(base) jovyan@xxxxxxxxxxxx:~/work$`
- To clean up existing outputs and rendered Quarto reports, type `make clean` and press <kbd>ENTER</kbd>. 
- To render the `.qmd` source file into `PDF` and `HTML` formats, type `make all` and press <kbd>ENTER</kbd>. 
- After you finish your work, type `exit` and press <kbd>ENTER</kbd>.

## Dependencies
- Python 3.13.11, Jupyter and Python Packages listed in the default scipy notebook base Docker image [here](https://github.com/jupyter/docker-stacks/wiki/x86_64-default-scipy-notebook-0dd81e2dd718).
- [Quarto v1.8.26](https://quarto.org/docs/blog/posts/2025-10-13-1.8-release/).
- [TinyTeX v2026.03.02](https://github.com/rstudio/tinytex-releases/releases)

## Licenses
This project report is offered under 
the [Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
The code and software provided in this project are offered under the [MIT open source license](https://opensource.org/licenses/MIT). See [the license file](LICENSE.md) for more information. 
