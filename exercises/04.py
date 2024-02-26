#### Exercise 05. Does the dataset contain NAs? (★☆☆)

#Print a boolean value (`true` or `fase`) followed by the rows/cols that contains NAs.

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

nan_rows = ds.isna().any(axis=1)
print(nan_rows)
