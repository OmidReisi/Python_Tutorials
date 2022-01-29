import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from dmba import plotDecisionTree, classificationSummary
from sklearn.ensemble import RandomForestClassifier


eBay_Auctions_df = pd.read_csv(r"./eBayAuctions.csv")
eBay_Auctions_df = pd.get_dummies(eBay_Auctions_df, drop_first=False)

predictors = list(eBay_Auctions_df.columns.drop("Competitive?"))
outcome = "Competitive?"


x = eBay_Auctions_df[predictors]
y = eBay_Auctions_df[outcome]

train_x, valid_x, train_y, valid_y = train_test_split(
    x, y, test_size=0.4, random_state=1
)

rf = RandomForestClassifier(n_estimators=500, random_state=1)

rf.fit(train_x, train_y)

importances = rf.feature_importances_
std = np.std([tree.feature_importances_ for tree in rf.estimators_], axis=0)
feature_importance_df = pd.DataFrame(
    {"feature": train_x.columns, "importance": importances, "std": std}
)
feature_importance_df = feature_importance_df.sort_values("importance", ascending=False)

print(feature_importance_df)


predictors = ["OpenPrice", "ClosePrice"]
outcome = "Competitive?"


x = eBay_Auctions_df[predictors]
y = eBay_Auctions_df[outcome]


train_x, valid_x, train_y, valid_y = train_test_split(
    x, y, test_size=0.4, random_state=1
)

class_tree = DecisionTreeClassifier(max_depth=7, min_samples_split=50)
class_tree.fit(train_x, train_y)

# Image = plotDecisionTree(
#     class_tree, feature_names=train_x.columns, class_names=class_tree.classes_
# )

# with open(r"./3_3_fig.JPG", "wb") as file:
#     file.write(Image.data)


# print("training_data confusion matrix ...")
# classificationSummary(train_y, class_tree.predict(train_x))
# print("\n\n")


# print("validation_data confusion matrix ...")
# classificationSummary(valid_y, class_tree.predict(valid_x))

# from sklearn.tree import _tree


# def tree_to_code(tree, feature_names):
#     tree_ = tree.tree_
#     feature_name = [
#         feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
#         for i in tree_.feature
#     ]
#     print("def tree({}):".format(", ".join(feature_names)))

#     def recurse(node, depth):
#         indent = "  " * depth
#         if tree_.feature[node] != _tree.TREE_UNDEFINED:
#             name = feature_name[node]
#             threshold = tree_.threshold[node]
#             print("{}if {} <= {}:".format(indent, name, threshold))
#             recurse(tree_.children_left[node], depth + 1)
#             print("{}else:  # if {} > {}".format(indent, name, threshold))
#             recurse(tree_.children_right[node], depth + 1)
#         else:
#             print("{}return {}".format(indent, tree_.value[node]))

#     recurse(0, 1)


# tree_to_code(class_tree, predictors)
