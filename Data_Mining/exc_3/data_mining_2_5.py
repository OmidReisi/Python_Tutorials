import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from dmba import classificationSummary


Universal_bank_df = pd.read_csv(r"./UniversalBank.csv")

Universal_bank_df.drop(columns=["ID", "ZIP Code"], inplace=True)

Universal_bank_df = pd.get_dummies(Universal_bank_df, drop_first=False)

predictors = Universal_bank_df.columns.drop("Personal Loan")
outcome = "Personal Loan"

cutoff = 0.5


x = Universal_bank_df[predictors]
y = Universal_bank_df[outcome]


train_x, temp_x, train_y, temp_y = train_test_split(x, y, test_size=0.5, random_state=1)
valid_x, test_x, valid_y, test_y = train_test_split(
    temp_x, temp_y, test_size=0.4, random_state=1
)

knn = KNeighborsRegressor(n_neighbors=29)
knn.fit(train_x, train_y)

print("training_data confusion matrix ...")
predicted_values = [0 if pred < cutoff else 1 for pred in knn.predict(train_x)]
classificationSummary(train_y, predicted_values)

print("\n\n")
print("validation_data confusion matrix ...")
predicted_values = [0 if pred < cutoff else 1 for pred in knn.predict(valid_x)]
classificationSummary(valid_y, predicted_values)

print("\n\n")
print("test_data confusion matrix ...")
predicted_values = [0 if pred < cutoff else 1 for pred in knn.predict(test_x)]
classificationSummary(test_y, predicted_values)
