import pandas as pd

print(pd.__version__)

df = pd.DataFrame(
    {"name": ["Alireza", "Sarah", "Mohammad"],
     "gpa": [19.8, 15.3, 17.5],
     "age": [28, 22, 25]
     }
)

print(df, type(df))

print(df["age"], type(df["age"]))

ds = pd.Series(["phd", "bc", "ms"], name="degree")
print(ds)
