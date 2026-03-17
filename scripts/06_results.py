import pandas as pd
import matplotlib.pyplot as plt
import click
from pathlib import Path

@click.command()
@click.option(
    "--predictions_path",
    required=True,
    type=click.Path(exists=True)
)
@click.option(
    "--outputs_path",
    required=True,
    type=click.Path()
)
@click.option(
    "--fig_name",
    required=True,
    type=click.Path()
)

def results(predictions_path, outputs_path, fig_name):
    # import predictions for plot visualization
    y_preds_df = pd.read_csv(predictions_path)
    y_pred = y_preds_df["y_pred"]
    y_test = y_preds_df["y_true"]
    
    # make figure 4 - accuracy plot
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # perfect prediction line
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Figure 4: Actual vs Predicted Ranks')
    
    # make directory to save the plot
    outputs_path = Path(outputs_path)
    outputs_path.mkdir(parents=True, exist_ok=True)
    plt.savefig(outputs_path / fig_name)

if __name__ == "__main__":
    results()