from pathlib import Path

import pandas as pd

dpath = Path("../data")

students = pd.read_csv(dpath / "students.csv")
print(students.head())

X = students.drop("Gender", axis="columns")
y = students["Gender"]

print(X.head())
print(y.head())
