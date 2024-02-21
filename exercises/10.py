#### Exercise 11. Analyse the relation between the surface and the price of the houses (★★☆)

#Hint: You can make a `scatter plot` and then write a conclusion about it

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

a = ds.plot.scatter(x="surface", y="price")

