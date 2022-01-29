import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors


Universal_bank_df = pd.read_csv(r"./UniversalBank.csv")

Universal_bank_df.drop(columns=["ID", "ZIP Code"], inplace=True)

Universal_bank_df = pd.get_dummies(Universal_bank_df, drop_first=False)

predictors = Universal_bank_df.columns.drop("Personal Loan")
outcome = "Personal Loan"

new_customer = pd.DataFrame(
    [
        {
            "Age": 40,
            "Experience": 10,
            "Income": 84,
            "Family": 2,
            "CCAvg": 2,
            "Education": 2,
            "Mortgage": 0,
            "Securities Account": 0,
            "CD Account": 0,
            "Online": 1,
            "CreditCard": 1,
        }
    ]
)

x = Universal_bank_df[predictors]
y = Universal_bank_df[outcome]

train_x, valid_x, train_y, valid_y = train_test_split(
    x, y, test_size=0.4, random_state=1
)


knn = NearestNeighbors(n_neighbors=1)
knn.fit(train_x)

distances, indices = knn.kneighbors(new_customer)

print("indices: ", indices[0])
print("distances :", distances[0])

new_customer["Personal Loan"] = Universal_bank_df.iloc[1463]["Personal Loan"]
print(
    f"The new_customer that is given is closest to the {int(indices[0][0])}th data with distance of {distances[0][0]:.2f}, and it's Personal Loan field is {int(new_customer.iloc[0]['Personal Loan'])}"
)
