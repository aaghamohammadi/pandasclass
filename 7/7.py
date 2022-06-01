from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

print(df['state'])

print(df[['state', 'death']])
print(df.loc[3:5, ['state', 'death']])
print(df.iloc[:5, [0, 1]])
