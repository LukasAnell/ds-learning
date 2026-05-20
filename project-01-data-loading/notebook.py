# %% Imports
import pandas as pd

# %% Load data
df = pd.read_csv("data/2019.csv")

# %% Shape
print(df.shape)

# %% First and last rows
print(df.head(1))
print(df.tail(1))

# %% Column names and types
print(df.columns.tolist())
print(df.dtypes)

# %% Null counts
print(df.isnull().sum())
