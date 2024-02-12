#### Exercise 03. Which is the biggest and the smallest house in the dataset?

# level4 == Location
# surface

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

#Get the id and the price of the house with the biggest
index_high = ds['surface'].idxmax()
surface_high = ds['surface'].max()

#Getting the house address from the index collected in previous step
address_high = ds['address'].loc[index_high]

print("The house with address" ,address_high, "is the biggest and its surface is",surface_high, "meters")

#Get the id and the price of the house with the highest price
index_low = ds['price'].idxmin()
surface_low = ds['price'].min()

#Getting the house address from the index collected in previous step
address_low = ds['address'].loc[index_low]

print("The house with address" ,address_low, "is the smallest and its surface is",surface_low, "meters")
