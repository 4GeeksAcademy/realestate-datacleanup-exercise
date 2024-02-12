import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

#print(ds.head(5))

#Get the id and the price of the house with the highest price
index = ds['price'].idxmax()
price = ds['price'].max()
print(ds.loc[index])

#Getting the house address from the index collected in previous step
address = ds['address'].loc[index]