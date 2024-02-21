#### Exercise 14. Now let's work with the "south belt" of madrid. Make a subset of the original DataFrame that contains the following populations (level5 column): "Fuenlabrada","Leganés","Getafe","Alcorcón" (★★☆)

# Hint: Filter the original DataFrame using the column `level5` and the function `isin`

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

southbelt = ds["level5"].isin(["Fuenlabrada","Leganés","Getafe","Alcorcón"])
