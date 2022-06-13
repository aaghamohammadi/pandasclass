from pathlib import Path

import numpy as np
import pandas as pd

dpath = Path("../data")

students = pd.read_csv(dpath / "students.csv")
print(students)
print(students["Gender"])

students["is_male"] = 1
students.loc[students['Gender'] == "Female", "is_male"] = 0
print(students["is_male"])

print(students["college mark"])

conditions = [
    (students["college mark"] < 50),
    (students["college mark"] >= 50) & (students["college mark"] < 60),
    (students["college mark"] >= 60) & (students["college mark"] < 70),
    (students["college mark"] >= 70) & (students["college mark"] < 80),
    (students["college mark"] >= 80),
]

values = [
    "F",
    "D",
    "C",
    "B",
    "A",
]

students["college_score"] = np.select(conditions, values)
print(students["college_score"])
