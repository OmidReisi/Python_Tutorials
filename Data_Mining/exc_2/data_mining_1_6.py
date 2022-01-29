import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cereals_df = pd.read_csv(r"./cereals.csv")
cereals_df.drop(cereals_df.columns[[0, 1, 2, 12]], axis=1, inplace=True)

fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(
    cereals_df.corr(),
    xticklabels=cereals_df.columns,
    yticklabels=cereals_df.columns,
    annot=True,
    ax=ax,
)
plt.show()
