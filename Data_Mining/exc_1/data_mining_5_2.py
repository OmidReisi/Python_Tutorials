import pandas as pd
from sklearn.model_selection import train_test_split

Toyota_Corolla_df = pd.read_csv(r"./ToyotaCorolla.csv")

Toyota_Corolla_df.columns = [
    s.strip().replace(" ", "_") for s in Toyota_Corolla_df.columns
]

training_data, temp_data = train_test_split(
    Toyota_Corolla_df, test_size=0.5, random_state=1
)

test_data, evaluation_data = train_test_split(temp_data, test_size=0.4, random_state=1)

print("training_data : ", training_data.shape)
print("test_data : ", test_data.shape)
print("evaluation_data : ", evaluation_data.shape)
