# %% Imports
import pandas as pd

# %% Load data
df = pd.read_csv("data/2019.csv")

# %% Shape
print(df.shape)

# %% First and last rows
print(df.head(5))
print(df.tail(5))

# %% Column names and types
print(df.info())

# %% Null counts
print(df.isnull().sum())
