#### Exercise 07. Which is the mean of prices in the population (level5 column) of "Arroyomolinos (Madrid)"? (★★☆)

#Print the obtained value

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

value = ds.loc[ds['level5'] == 'Arroyomolinos (Madrid)', 'price'].mean()
print(value)