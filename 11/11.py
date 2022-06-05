from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

print(df.select_dtypes(include="object"))
print(df.select_dtypes(include=["integer", "object"]))
print(df.select_dtypes(include="number"))
print(df.select_dtypes(exclude="integer"))

print(df.filter(items=["date", "state"]))
print(df.filter(like="death"))
print(df.filter(regex=r"[nN]egative"))
