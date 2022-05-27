from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

print(df.head())
print(df.tail())

print(df.dtypes)
print(df.dtypes.value_counts())

df.info()
