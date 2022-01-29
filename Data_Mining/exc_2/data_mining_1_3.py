import pandas as pd
import matplotlib.pyplot as plt

cereals_df = pd.read_csv(r"./cereals.csv")

# removing non-numeric variables from the data frame
cereals_df.drop(cereals_df.columns[[0, 1, 2, 12, 15]], axis=1, inplace=True)

fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(10, 8))

axs = axs.ravel()

for variable_pair in enumerate(cereals_df.columns):
    axs[variable_pair[0]].hist(cereals_df[variable_pair[1]], edgecolor="black")
    axs[variable_pair[0]].set_xlabel(variable_pair[1])
    axs[variable_pair[0]].set_ylabel("count")
    axs[variable_pair[0]].set_title(f"Histogram of {variable_pair[1]}")
    axs[variable_pair[0]].tick_params(axis="x", rotation=45)

fig.delaxes(axs[11])

fig.tight_layout()
plt.show()
