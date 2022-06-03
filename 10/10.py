from pathlib import Path

import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

dth = (df["death"] / df["positive"]) * 100

df = df.assign(death_to_positive=dth)
print(df["death_to_positive"].describe())


def gt_100(data_frame):
    return data_frame["death"] >= 100


print(df.assign(death_gt_100=gt_100))

print(df.drop("date", axis="columns"))
