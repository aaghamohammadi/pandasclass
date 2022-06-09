from pathlib import Path

import numpy as np
import pandas as pd

dpath = Path("../data")

df = pd.read_csv(dpath / "all-states-history.csv")

# split - apply - combine
print(df.groupby(['state'])['death'].sum().sort_values(ascending=False))

group = df.groupby(['state'])
print(group)
print(group.groups)
print(group.get_group("NY"))

print(df.groupby(['state'])['death'].agg([np.sum, np.mean, np.max, np.size]))
