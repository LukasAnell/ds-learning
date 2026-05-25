# %% Imports
import pandas as pd

# %% Load data
df = pd.read_csv("data/311.csv", nrows=100000)

# %% Print head of table
df.head()

# %% Assess missing values
# Print out which columns in df have at least one null value
print(df.isnull().sum().sort_values(ascending=False))
print(f"\nTotal rows: {len(df)}")

# %% Handle missing values
...

# %% Handle duplicates
df = df.drop_duplicates(inplace=True)

# %% Fix data types
...

# %% Rename columns to snake_case
...

# %% Before/after summary
...

# %% Save cleaned data
df.to_csv("data/311_clean.csv", index=False)
