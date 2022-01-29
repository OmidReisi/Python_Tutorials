import pandas as pd
import matplotlib.pyplot as plt

Riding_Mowers_df = pd.read_csv(r"./RidingMowers .csv")

plt.scatter(
    x=[data.Income for data in Riding_Mowers_df.iloc if data.Ownership == "Owner"],
    y=[data.Lot_Size for data in Riding_Mowers_df.iloc if data.Ownership == "Owner"],
    c="red",
)

plt.scatter(
    x=[data.Income for data in Riding_Mowers_df.iloc if data.Ownership == "Nonowner"],
    y=[data.Lot_Size for data in Riding_Mowers_df.iloc if data.Ownership == "Nonowner"],
    c="blue",
)

plt.legend(["Owner", "Nonowner"])
plt.show()
