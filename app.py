import pandas as pd

# Ejercicio 00 Lectura y visualización del archivo csv
# This CSV file contains semicolons instead of comas as separator
df = pd.read_csv('assets/real_estate.csv', sep=';')
#print(df)

# Exercise 01. Which is the most expensive house in the dataset?

expensive_price = df['price'].max() # Esto me da el precio maximo

index_expensive = df['price'].idxmax() # Esto me da el índice donde está el precio maximo

# Con el indice puedo saber la direccion de la casa

direccion_expensive = df.loc[index_expensive, 'address']

print(f"The house with address {direccion_expensive} is the most expensive and its price is {expensive_price} USD")

# Exercise 02. Which is the cheapest house in the dataset?
cheapest_price = df['price'].min() # Esto me da el precio minimo

index_cheapest = df['price'].idxmin() # Esto me da el índice donde está el precio minimo

# Con el indice puedo saber la direccion de la casa

direccion_cheapest = df.loc[index_cheapest, 'address']

print(f"The house with address {direccion_cheapest} is the cheapest and its price is {cheapest_price} USD")

# Exercise 03. Which is the biggest and the smallest house in the dataset?
smallest_surface = df['surface'].min() # Esto me da la superficie minima
biggest_surface = df['surface'].max() # Esto me da la superficie maxima

index_smallest = df['surface'].idxmin() # Esto me da el índice donde está la superficie minima
index_biggest = df['surface'].idxmax() # Esto me da el índice donde está la superficie maxima

# Con el indice puedo saber la direccion de la casa
direccion_smallest = df.loc[index_smallest, 'address']
direccion_biggest = df.loc[index_biggest, 'address']

print(f"The smallest house is located on {direccion_smallest} and its surface is {smallest_surface} meters")

print(f"The biggest house is located on {direccion_biggest} and its surface is {biggest_surface} meters")

# Exercise 04. How many populations (level5 column) the dataset contains?