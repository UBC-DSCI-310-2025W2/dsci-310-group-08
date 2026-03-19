# author: Shivani Aggarwal, Luna Gulec, Jingyuan Liu, Sarenna Ulman
# date: 2026-03-15

.PHONY: all clean

all: data/raw/parks_raw.csv \
	data/processed/parks_processed.csv \
	data/raw/data_dict.csv \
	docs/index.html \
	docs/index.pdf \
# 	data/processed/splits/X_train.csv data/processed/splits/y_train.csv data/processed/splits/X_test.csv data/processed/splits/y_test.csv \
# 	outputs/eda/01_rank_frequency.png outputs/eda/02_rank-last-time_frequency.png outputs/eda/03_numerical_boxplots.png \
# 	data/processed/predictions/test_predictions.csv \
# 	outputs/results/04_actual-vs-predicted.png 

# run scripts

# script 01
data/raw/parks_raw.csv data/raw/data_dict.csv: scripts/01_download-data.py
	python scripts/01_download-data.py \
		--input_path="https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2021/2021-06-22/parks.csv" \
		--output_path=data/raw/parks_raw.csv\
		--output_path_data_dict=data/raw/data_dict.csv
		

# script 02
data/processed/parks_processed.csv: data/raw/parks_raw.csv scripts/02_process-data.py
	python scripts/02_process-data.py \
		--raw_path=data/raw/parks_raw.csv \
		--processed_path=data/processed/parks_processed.csv

# # script 03
# data/processed/splits/X_train.csv data/processed/splits/y_train.csv data/processed/splits/X_test.csv data/processed/splits/y_test.csv: data/processed/parks_processed.csv scripts/03_split-data.py
# 	python scripts/03_split-data.py \
# 		--data_path=data/processed/parks_processed.csv \
# 		--splits_path=data/processed/splits

# # script 04
# outputs/eda/01_rank_frequency.png outputs/eda/02_rank-last-time_frequency.png outputs/eda/03_numerical_boxplots.png: data/processed/splits/X_train.csv data/processed/splits/y_train.csv scripts/04_eda.py
# 	python scripts/04_eda.py \
# 		--splits_path=data/processed/splits \
# 		--outputs_path=outputs/eda \
# 		--fig1_name=01_rank_frequency.png \
# 		--fig2_name=02_rank-last-time_frequency.png \
# 		--fig3_name=03_numerical_boxplots.png

# # script 05
# data/processed/predictions/test_predictions.csv: data/processed/splits/X_train.csv data/processed/splits/y_train.csv data/processed/splits/X_test.csv data/processed/splits/y_test.csv scripts/05_regression.py
# 	python scripts/05_regression.py \
# 		--splits_path=data/processed/splits \
# 		--predictions_path=data/processed/predictions/test_predictions.csv

# # script 06
# outputs/results/04_actual-vs-predicted.png: data/processed/predictions/test_predictions.csv scripts/06_results.py
# 	python scripts/06_results.py \
# 		--predictions_path=data/processed/predictions/test_predictions.csv \
# 		--outputs_path=outputs/results \
# 		--fig_name=04_actual-vs-predicted.png

# render quarto report in HTML and PDF
docs/index.html: reports/parks_analysis.qmd data outputs
	quarto render reports/parks_analysis.qmd --to html --output-dir ../docs/ 
	mv docs/parks_analysis.html docs/index.html

docs/index.pdf: reports/parks_analysis.qmd data outputs
	quarto render reports/parks_analysis.qmd --to pdf --output-dir ../docs/ 
	mv docs/parks_analysis.pdf docs/index.pdf

# clean
clean:
	rm -rf docs
	rm -rf data/processed/predictions
	rm -rf data/processed/splits
	rm -f data/raw/*.csv
	rm -f data/processed/*.csv
	rm -f outputs/**/*.csv
	rm -f outputs/**/*.png
