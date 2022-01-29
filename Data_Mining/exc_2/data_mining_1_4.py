import pandas as pd
import matplotlib.pyplot as plt


cereals_df = pd.read_csv(r"./cereals.csv")

data_hot = [d.calories for d in cereals_df.iloc if d.type == "H"]
data_cold = [d.calories for d in cereals_df.iloc if d.type == "C"]

data_for_plot = [data_hot, data_cold]

plt.boxplot(data_for_plot, labels=["HOT", "COLD"])
plt.xlabel("Type")
plt.ylabel("Calories")
plt.xticks(rotation=90)
plt.show()
