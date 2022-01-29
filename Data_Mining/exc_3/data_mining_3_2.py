import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from dmba import plotDecisionTree, classificationSummary


eBay_Auctions_df = pd.read_csv(r"./eBayAuctions.csv")
eBay_Auctions_df = pd.get_dummies(eBay_Auctions_df, drop_first=False)

predictors = list(eBay_Auctions_df.columns.drop("Competitive?"))
outcome = "Competitive?"


x = eBay_Auctions_df[predictors]
y = eBay_Auctions_df[outcome]

train_x, valid_x, train_y, valid_y = train_test_split(
    x, y, test_size=0.4, random_state=1
)

class_tree = DecisionTreeClassifier(max_depth=7, min_samples_split=50)
class_tree.fit(train_x, train_y)

print("training_data confusion matrix ...")
classificationSummary(train_y, class_tree.predict(train_x))
print("\n\n")


print("validation_data confusion matrix ...")
classificationSummary(valid_y, class_tree.predict(valid_x))
