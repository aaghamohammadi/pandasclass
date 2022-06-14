from pathlib import Path

import pandas as pd

dpath = Path("../data")

students = pd.read_csv(dpath / "students.csv")

col = "prefer to study in"
students[col] = students[col].map({"Morning": "M", "Anytime": "A", "Night": "N"})
print(students[col])


def transform_height(height):
    if height >= 170:
        return "tall"
    if 160 <= height < 170:
        return "medium"
    return "short"


col = "Height(CM)"

students[col] = students[col].map(transform_height)
print(students[col])
