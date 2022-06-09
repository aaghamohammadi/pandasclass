from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

# and, or, not
# &, |, ~

criterion1 = (df["state"] == "WA") | (df["state"] == "AZ")
criterion2 = df["death"] > 50
condition = criterion1 & criterion2
print(condition)
print(condition.value_counts())
print(df[condition])
