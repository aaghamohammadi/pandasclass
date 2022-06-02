from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

print(df['death'] / df['death'].max())  # print(df['death'].div(df['death'].max()))

print(df['death'] >= 100)  # print(df['death'].ge(100))
print(df['state'] == "WA")  # print(df['state'].eq("WA"))
