import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


Laptop_Sales_df = pd.read_csv(r"./LaptopSalesJanuary2008.csv")

Laptop_Sales_df.rename(
    columns={"Store Postcode": "SP", "Retail Price": "RP"}, inplace=True
)


data_for_plot = []

for store_postcode in Laptop_Sales_df.SP.unique():
    data = [s.RP for s in Laptop_Sales_df.iloc if s.SP == store_postcode]
    data_for_plot.append(data)


plt.boxplot(data_for_plot, labels=Laptop_Sales_df.SP.unique())
plt.xlabel("Store Postcode")
plt.ylabel("Average Price Retail")
plt.xticks(rotation=90)

plt.show()
