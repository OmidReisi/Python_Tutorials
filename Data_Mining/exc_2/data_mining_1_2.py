import pandas as pd

cereals_df = pd.read_csv(r"./cereals.csv")

# removing non-numeric variables from the data frame
cereals_df.drop(cereals_df.columns[[0, 1, 2, 12, 15]], axis=1, inplace=True)

cereals_df.describe()
