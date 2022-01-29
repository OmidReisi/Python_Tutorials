import pandas as pd
import matplotlib.pyplot as plt


Laptop_Sales_df = pd.read_csv(r"./LaptopSalesJanuary2008.csv")

Laptop_Sales_df.rename(
    columns={"Store Postcode": "SP", "Retail Price": "RP"}, inplace=True
)

data_for_plot = Laptop_Sales_df.groupby("SP").mean()["RP"].sort_values()

plt.bar(data_for_plot.index, data_for_plot)
plt.xlabel("Store Postcode")
plt.ylabel("Average Price Retail")
plt.xticks(rotation=90)


plt.show()
