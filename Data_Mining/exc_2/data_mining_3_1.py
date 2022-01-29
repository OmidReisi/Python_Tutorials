import pandas as pd
from dmba import classificationSummary


prediction_df = pd.read_csv(r"./prediction_table.csv")

cutoffs = [0.25, 0.50, 0.75]

for cutoff in cutoffs:
    predicted_values = [1 if p > cutoff else 0 for p in prediction_df.propensity_1]

    print(f"Classification Summary for cutoff = {cutoff}")
    classificationSummary(
        prediction_df.actual_class, predicted_values, class_names=["class 0", "class 1"]
    )
    print()
