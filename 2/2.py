from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")
print(df)

print(df.index)  # index
print(df.columns)  # columns
print(df.to_numpy())  # data

print(issubclass(pd.RangeIndex, pd.Index))
print(issubclass(df.columns.__class__, pd.Index))
