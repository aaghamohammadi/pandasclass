from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

print(df.isna().sum())
print(df.fillna(0))

col_names = ["death", "totalTestsAntibody"]

print(df[col_names].dropna(how="any"))
print(df[col_names].dropna(how="all"))
