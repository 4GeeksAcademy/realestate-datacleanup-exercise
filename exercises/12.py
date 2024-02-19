#### Exercise 13. Which is the population (level5 column) that contains the most houses? (★★☆)

#Print both the population and the number of houses

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

group = ds.groupby('level5')
print(group.groups)