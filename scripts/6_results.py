import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# import predictions for plot visualization
y_preds_df = pd.read_csv("../predictions/test_predictions.csv")
y_pred = y_preds_df["y_pred"]
y_test = y_preds_df["y_true"]

# make figure 4 - accuracy plot
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # perfect prediction line
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Figure 4: Actual vs Predicted Ranks')

# make directory to save the plot
Path("../artifacts/results").mkdir(parents=True, exist_ok=True)
plt.savefig("../artifacts/results/4_actual-vs-predicted.png")