import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


Toyota_Corolla_df = pd.read_csv(r"./ToyotaCorolla.csv")

predictors = [
    "Age_08_04",
    "KM",
    "Fuel_Type",
    "HP",
    "Automatic",
    "Doors",
    "Quarterly_Tax",
    "Mfr_Guarantee",
    "Guarantee_Period",
    "Airco",
    "Automatic_airco",
    "CD_Player",
    "Powered_Windows",
    "Sport_Model",
    "Tow_Bar",
]

outcome = "Price"

x = pd.get_dummies(Toyota_Corolla_df[predictors], drop_first=True)
y = Toyota_Corolla_df[outcome]

train_x, temp_x, train_y, temp_y = train_test_split(x, y, test_size=0.5, random_state=1)
valid_x, test_x, valid_y, test_y = train_test_split(
    temp_x, temp_y, test_size=0.4, random_state=1
)


Toyota_Corolla_lm = LinearRegression()
Toyota_Corolla_lm.fit(train_x, train_y)

predictor_coef_df = pd.DataFrame(
    {"Predictor": x.columns, "Coefficient": Toyota_Corolla_lm.coef_}
)


print(predictor_coef_df.sort_values("Coefficient", ascending=False))

