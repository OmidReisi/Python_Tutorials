import pandas as pd
import matplotlib.pyplot as plt


cereals_df = pd.read_csv(r"./cereals.csv")

data_1 = [d.rating for d in cereals_df.iloc if d.shelf == 1]
data_2 = [d.rating for d in cereals_df.iloc if d.shelf == 2]
data_3 = [d.rating for d in cereals_df.iloc if d.shelf == 3]

data_for_plot = [data_1, data_2, data_3]

plt.boxplot(data_for_plot, labels=["1", "2", "3"])
plt.xlabel("Shelf Level")
plt.ylabel("Customer's Rating")
plt.show()
