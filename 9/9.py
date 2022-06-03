from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

print(df.rename(columns={
    "deathConfirmed": "death_confirmed",
    "deathIncrease": "death_increase"
}).columns)

print(df.set_index("state").rename(index={"AK": "Alaska"}).head(5))


def upper(value):
    return value.upper()


print(df.rename(columns=upper).columns)
