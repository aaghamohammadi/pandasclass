from pathlib import Path

import numpy as np
import pandas as pd

dpath = Path("../data")
df = pd.read_csv(dpath / "iris.csv")

print(df["sepal.length"].min(), df["sepal.length"].max())

print(df["petal.length"].std())

print(df.drop(6, axis="index"))

df.info()

print(df.dtypes)

gm = np.sqrt(df["sepal.width"] * df["sepal.length"])
df = df.assign(geometric_mean=gm)
print(df)

total = ((df["petal.width"] < 1.5) * (df['variety'] == "Versicolor")).sum()
print(total / len(df) * 100)
