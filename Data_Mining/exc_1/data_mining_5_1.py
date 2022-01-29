import pandas as pd


Toyota_Corolla_df = pd.read_csv(r"./ToyotaCorolla.csv")

Toyota_Corolla_df.columns = [
    s.strip().replace(" ", "_") for s in Toyota_Corolla_df.columns
]

Toyota_Corolla_df_temp = pd.get_dummies(
    Toyota_Corolla_df.iloc[:, 2:], prefix_sep="_", drop_first=True
)

Toyota_Corolla_df = pd.concat(
    [Toyota_Corolla_df.iloc[:, :2], Toyota_Corolla_df_temp], axis=1
)

print(Toyota_Corolla_df)
