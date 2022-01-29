import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import accuracy_score
from dmba import classificationSummary, regressionSummary


Universal_bank_df = pd.read_csv(r"./UniversalBank.csv")

Universal_bank_df.drop(columns=["ID", "ZIP Code"], inplace=True)

Universal_bank_df = pd.get_dummies(Universal_bank_df, drop_first=False)

predictors = Universal_bank_df.columns.drop("Personal Loan")
outcome = "Personal Loan"

cutoff = 0.5


x = Universal_bank_df[predictors]
y = Universal_bank_df[outcome]

train_x, valid_x, train_y, valid_y = train_test_split(
    x, y, test_size=0.4, random_state=1
)


knn = KNeighborsRegressor(n_neighbors=29)
knn.fit(train_x, train_y)


predicted_values = [0 if pred < cutoff else 1 for pred in knn.predict(valid_x)]

classificationSummary(valid_y, predicted_values)
regressionSummary(valid_y, predicted_values)
