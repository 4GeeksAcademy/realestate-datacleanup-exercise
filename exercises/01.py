import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

#Get the id and the price of the house with the highest price
index = ds['price'].idxmin()
price = ds['price'].min()

#Getting the house address from the index collected in previous step
address = ds['address'].loc[index]

# TO DO, the price is 0 so it might be duplicated
print("The house with address" ,address, "is the cheapest and its price is",price)