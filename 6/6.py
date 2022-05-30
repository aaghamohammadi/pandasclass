from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

print(df.shape, len(df), df['state'].size)

print(df['state'].value_counts(), df['state'].value_counts(normalize=True))

print(df['totalTestsViral'].count())  # number of non-missing values

print(df['totalTestsViral'].min(), df['totalTestsViral'].max(), df['totalTestsViral'].mean())

print(df['totalTestsViral'].describe())

print(df['totalTestsViral'].quantile([0.1, 0.2, 0.5]))
