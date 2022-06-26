from pathlib import Path

import pandas as pd

dpath = Path("../data")

students = pd.read_csv(dpath / "students.csv")

pivot1 = pd.pivot_table(data=students, index="Gender", values="Height(CM)")
print(pivot1)

pivot2 = pd.pivot_table(data=students, index="Gender", values="Height(CM)", columns="Department")
print(pivot2)

target_column = "salary expectation"
pivot3 = pd.pivot_table(data=students,
                        index="Gender",
                        values=target_column,
                        columns="Department",
                        aggfunc=["mean"],
                        margins=True, margins_name="total")
print(pivot3.T.head())
