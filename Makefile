# author: Shivani Aggarwal, Luna Gulec, Jingyuan Liu, Sarenna Ulman (DSCI_V 310 101 2025W2 Group 08)
# date: 2026-03-15

.PHONY: all clean

# run the whole analysis and render the report
all: docs/index.html \
	docs/index.pdf

# script 01
# read in the raw data from its URL and save its data dictionary as a .csv file
data/raw/parks_raw.csv data/raw/data_dict.csv: scripts/01_download-data.py
	python scripts/01_download-data.py \
		--input_path="https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2021/2021-06-22/parks.csv" \
		--output_path=data/raw/parks_raw.csv\
		--output_path_data_dict=data/raw/data_dict.csv
		
# script 02
# perform data pre-processing and save the processed data as a .csv file in the /data/processed directory
data/processed/parks_processed.csv: data/raw/parks_raw.csv scripts/02_process-data.py
	python scripts/02_process-data.py \
		--raw_path=data/raw/parks_raw.csv \
		--processed_path=data/processed/parks_processed.csv

# script 03
# split the processed data into training and testing sets and separate explanatory variables from the target column
# and save them into separate .csv files
data/processed/splits/X_train.csv data/processed/splits/y_train.csv data/processed/splits/X_test.csv data/processed/splits/y_test.csv: data/processed/validation_passed.txt scripts/03_split-data.py
	python scripts/03_split-data.py \
		--data_path=data/processed/parks_processed.csv \
		--splits_path=data/processed/splits

# script 04
# perform explanatory data analysis (EDA), save relative visualizations (plots) as .png files
# and a data summary table as a .csv file for EDA in the /outputs/eda directory
outputs/eda/01_rank_frequency.png outputs/eda/02_rank-last-time_frequency.png outputs/eda/03_rank_rank-last-time_scatter.png outputs/eda/04_numerical_boxplots.png outputs/eda/X_train_summary.csv: data/processed/splits/X_train.csv data/processed/splits/y_train.csv scripts/04_eda.py
	python scripts/04_eda.py \
		--splits_path=data/processed/splits \
		--outputs_path=outputs/eda \
		--fig1_name=01_rank_frequency.png \
		--fig2_name=02_rank-last-time_frequency.png \
		--fig3_name=03_rank_rank-last-time_scatter.png \
		--fig4_name=04_numerical_boxplots.png

# script 05
# fit the model, abstract the optimal hyperparameter and feature coefficients of the model from fitting 
# and save the predictions on the testing set as a .csv file
outputs/results/grid_search_results.csv outputs/results/model_coef.csv data/processed/predictions/test_predictions.csv: data/processed/splits/X_train.csv data/processed/splits/y_train.csv data/processed/splits/X_test.csv data/processed/splits/y_test.csv scripts/05_regression.py
	python scripts/05_regression.py \
		--splits_path=data/processed/splits \
		--predictions_path=data/processed/predictions \
		--predictions_result_path=outputs/results

# script 06
# generate the resulting actual vs prediction plot and save it as a .png file in the /outputs/results directory
outputs/results/05_actual-vs-predicted.png: data/processed/predictions/test_predictions.csv scripts/06_results.py
	python scripts/06_results.py \
		--predictions_path=data/processed/predictions/test_predictions.csv \
		--outputs_path=outputs/results \
		--fig_name=05_actual-vs-predicted.png

# script 07
# data validation of processed dataset
data/processed/validation_passed.txt: data/processed/parks_processed.csv scripts/07_data_validation.py
	python scripts/07_data_validation.py \
		--processed_path=data/processed/parks_processed.csv \
		--output_path=data/processed/validation_passed.txt

# render the HTML report from the Quarto .qmd file and move it to the docs folder
docs/index.html: reports/parks_analysis.qmd data/raw/parks_raw.csv data/raw/data_dict.csv \
	data/processed/parks_processed.csv \
	data/processed/splits/X_train.csv data/processed/splits/y_train.csv data/processed/splits/X_test.csv data/processed/splits/y_test.csv \
	outputs/eda/01_rank_frequency.png outputs/eda/02_rank-last-time_frequency.png outputs/eda/03_rank_rank-last-time_scatter.png outputs/eda/04_numerical_boxplots.png outputs/eda/X_train_summary.csv\
	outputs/results/grid_search_results.csv outputs/results/model_coef.csv data/processed/predictions/test_predictions.csv \
	outputs/results/05_actual-vs-predicted.png 
	quarto render reports/parks_analysis.qmd --to html --output-dir ../docs/ 
	mv docs/parks_analysis.html docs/index.html

# render the PDF report from the Quarto .qmd file and move it to the docs folder
docs/index.pdf: reports/parks_analysis.qmd data/raw/parks_raw.csv data/raw/data_dict.csv \
	data/processed/parks_processed.csv \
	data/processed/splits/X_train.csv data/processed/splits/y_train.csv data/processed/splits/X_test.csv data/processed/splits/y_test.csv \
	outputs/eda/01_rank_frequency.png outputs/eda/02_rank-last-time_frequency.png outputs/eda/03_rank_rank-last-time_scatter.png outputs/eda/04_numerical_boxplots.png outputs/eda/X_train_summary.csv\
	outputs/results/grid_search_results.csv outputs/results/model_coef.csv data/processed/predictions/test_predictions.csv \
	outputs/results/05_actual-vs-predicted.png 
	quarto render reports/parks_analysis.qmd --to pdf --output-dir ../docs/ 
	mv docs/parks_analysis.pdf docs/index.pdf

# clean up analysis
# remove all intermediate files generated in the analysis
clean:
	rm -rf docs
	rm -f data/raw/*.csv
	rm -f data/processed/*.csv
	rm -f data/processed/*.txt
	rm -rf data/processed/splits
	rm -rf data/processed/predictions
	rm -f outputs/**/*.csv
	rm -f outputs/**/*.png
	rm -rf reports/parks_analysis_files
