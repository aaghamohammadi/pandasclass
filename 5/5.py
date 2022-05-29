from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

df.to_excel(dpath / "all-states-history.xlsx", index=False, sheet_name="covid")

df = pd.read_excel(dpath / "all-states-history.xlsx", sheet_name="covid")
print(df)
