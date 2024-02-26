#### Exercise 04. How many populations (level5 column) the dataset contains? (★☆☆)

#Print the name of the populations with comma as separator. For example:

#`> print(populations)`

#`population1, population2, population3,...`

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

#Getting the unique values
populations = ds['level5'].unique()

#Convert the result into a list to add a comma between values
res = populations.tolist()
print(res)