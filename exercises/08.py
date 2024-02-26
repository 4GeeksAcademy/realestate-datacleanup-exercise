#### Exercise 09. Is the average of "Valdemorillo" and "Galapagar" prices the same? (★★☆)

#Print the both average prices and then write a conclusion about them

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')



value_val = ds.loc[ds['level5'] == 'Valdemorillo', 'price'].mean()
print(value_val)

value_gal = ds.loc[ds['level5'] == 'Galapagar', 'price'].mean()
print(value_gal)