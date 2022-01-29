import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from dmba import plotDecisionTree, classificationSummary


eBay_Auctions_df = pd.read_csv(r"./eBayAuctions.csv")
eBay_Auctions_df = pd.get_dummies(eBay_Auctions_df, drop_first=False)

predictors = ["OpenPrice", "ClosePrice"]
outcome = "Competitive?"


train_data, valid_data = train_test_split(
    eBay_Auctions_df, test_size=0.4, random_state=1
)

train_x = train_data[predictors]
train_y = train_data[outcome]
valid_x = valid_data[predictors]
valid_y = valid_data[outcome]


class_tree = DecisionTreeClassifier(max_depth=7, min_samples_split=50)
class_tree.fit(train_x, train_y)


plt.scatter(
    x=[data.ClosePrice for data in train_data.iloc if int(data["Competitive?"]) == 1],
    y=[data.OpenPrice for data in train_data.iloc if int(data["Competitive?"]) == 1],
    c="red",
)

plt.scatter(
    x=[data.ClosePrice for data in train_data.iloc if int(data["Competitive?"]) == 0],
    y=[data.OpenPrice for data in train_data.iloc if int(data["Competitive?"]) == 0],
    c="blue",
)

plt.legend(["Competitive", "Non-Competitive"])
plt.xlabel("ClosePrice")
plt.ylabel("OpenPrice")
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.show()
