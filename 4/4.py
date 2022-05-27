from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

print(df['state'])
print(df.state)

print(df.loc[:, "state"])
print(df.iloc[:5, 1])
