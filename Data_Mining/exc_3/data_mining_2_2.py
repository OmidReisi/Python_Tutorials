import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


Universal_bank_df = pd.read_csv(r"./UniversalBank.csv")

Universal_bank_df.drop(columns=["ID", "ZIP Code"], inplace=True)

Universal_bank_df = pd.get_dummies(Universal_bank_df, drop_first=False)

predictors = Universal_bank_df.columns.drop("Personal Loan")
outcome = "Personal Loan"


x = Universal_bank_df[predictors]
y = Universal_bank_df[outcome]

train_x, valid_x, train_y, valid_y = train_test_split(
    x, y, test_size=0.4, random_state=1
)

results = []

for k in range(1, 50):
    knn = KNeighborsClassifier(n_neighbors=k).fit(train_x, train_y)
    results.append({"k": k, "accuracy": accuracy_score(valid_y, knn.predict(valid_x))})


results_df = pd.DataFrame(results)

print(results_df.sort_values("accuracy", ascending=False))
