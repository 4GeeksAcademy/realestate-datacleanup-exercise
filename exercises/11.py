#### Exercise 12. How many real estate agencies the dataset contains? (★★☆)

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

real_state = ds['id_realEstates'].unique()

res = real_state.tolist()

print(len(res))