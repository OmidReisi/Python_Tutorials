import pandas as pd
from dmba import liftChart
import matplotlib.pyplot as plt


prediction_df = pd.read_csv(r"./prediction_table.csv")

prediction_df.sort_values(by=["propensity_1"], ascending=False, inplace=True)

fig, ax = plt.subplots()

liftChart(prediction_df.propensity_1, ax=ax)

ax.set_title("Lift Chart for Class Prediction")
ax.set_ylabel("Lift of Class 1 selection")
ax.set_xlabel("Percentage of Data")

plt.tight_layout()
plt.show()
