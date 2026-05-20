import os

import pandas as pd

df = pd.read_csv("data/2019.csv")

# Test 1: File structure
assert os.path.exists("summary.md"), "Missing summary.md"
assert os.path.exists("README.md"), "Missing README.md"

# Test 2: DataFrame loaded
assert df is not None, "DataFrame failed to load"
assert not df.empty, "DataFrame is empty"

# Test 3: Shape awareness
rows, cols = df.shape
assert rows > 0, "No rows found"
assert cols > 0, "No columns found"
print(f"Shape: {rows} rows, {cols} columns")

# Test 4: Null check
null_counts = df.isnull().sum()
assert isinstance(null_counts, pd.Series), "Null check didn't return a Series"
print("Null counts per column:")
print(null_counts)

# Test 5: First/last rows accessible
assert len(df.head(5)) == 5, "Couldn't retrieve first 5 rows"
assert len(df.tail(5)) == 5, "Couldn't retrieve last 5 rows"

print("\nAll tests passed!")
