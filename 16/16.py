from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")
dt = pd.to_datetime(df["date"])
df = df.assign(date=dt)
df = df \
    .assign(year=df["date"].dt.year) \
    .assign(month=df["date"].dt.month) \
    .assign(day=df["date"].dt.day) \
    .assign(week=df["date"].dt.isocalendar().week)

df = df.set_index(['date'])
print(df)
print(df.loc['2021'].groupby(["state"])["hospitalized"].sum())
