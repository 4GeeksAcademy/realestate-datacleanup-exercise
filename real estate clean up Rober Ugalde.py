# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 06:24:10 2024

@author: rober ugalde
"""

import pandas as pd

# This CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('C:/Users/rober ugalde/Documents/real_estate.csv', sep=';')
ds


#Exercise 01. Which is the most expensive house in the dataset? (★☆☆)
#Print the address and the price of the selected house. For example:
#The house with address General Street Nº5 is the most 
#expensive and its price is 5000000 USD



# Find the most expensive house
most_expensive = ds.loc[ds['price'].idxmax()]  # Assuming 'price' is the column with house prices

# Display the details of the most expensive house
address = most_expensive['address']  # Assuming 'address' is the column for house addresses
price = most_expensive['price']

print(f"The house with address {address} is the most expensive and its price is {price} USD.")



#Exercise 02. Which is the cheapest house in the dataset? (★☆☆)
#Print the address and the price of the selected house. For example:

#The house with address Concrete Street Nº1 is the cheapest and its price is 12000 USD


# Find the cheapest house
cheapest_house = ds.loc[ds['price'].idxmin()]  # Assuming 'price' is the column with house prices

# Extract details of the cheapest house
address = cheapest_house['address']  # Assuming 'address' is the column for house addresses
price = cheapest_house['price']

# Print the result
print(f"The house with address {address} is the cheapest and its price is {price} USD.")





#Exercise 03. Which is the biggest and the smallest house in the dataset? (★☆☆)
#Print both the address and the surface of the selected houses. For example:

#The biggest house is located on Yukka Street Nº10 and its surface is 5000 meters

#The smallest house is located on County Road 1 N and its surface is 200 meters









import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Find the biggest house
biggest_house = ds.loc[ds['surface'].idxmax()]  # Assuming 'surface' is the column for house surface areas
biggest_address = biggest_house['address']  # Assuming 'address' is the column for house addresses
biggest_surface = biggest_house['surface']

# Find the smallest house
smallest_house = ds.loc[ds['surface'].idxmin()]
smallest_address = smallest_house['address']
smallest_surface = smallest_house['surface']

# Print the results
print(f"The biggest house is located on {biggest_address} and its surface is {biggest_surface} meters.")
print(f"The smallest house is located on {smallest_address} and its surface is {smallest_surface} meters.")



#Exercise 04. How many populations (level5 column) the dataset contains? (★☆☆)
#Print the names of the populations with a comma as a separator. For example:

#> print(populations)

#population1, population2, population3, ...


import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Get unique populations from the 'level5' column
populations = ds['level5'].unique()  # Assuming 'level5' is the column for populations

# Convert the array to a comma-separated string
populations_list = ', '.join(populations)

# Print the names of the populations
print(f"Populations: {populations_list}")

# Print the total number of unique populations
print(f"Number of populations: {len(populations)}")


#Exercise 05. Does the dataset contain NAs? (★☆☆)
#Print a boolean value (True or False) followed by the rows/cols that contains NAs.

import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Check if the dataset contains any NAs
contains_nas = ds.isnull().values.any()

# Print whether the dataset contains NAs
print(f"Contains NAs: {contains_nas}")

if contains_nas:
    # Print rows with NAs
    rows_with_nas = ds[ds.isnull().any(axis=1)]
    print("\nRows with NAs:")
    print(rows_with_nas)
    
    # Print columns with NAs
    cols_with_nas = ds.columns[ds.isnull().any()].tolist()
    print("\nColumns with NAs:")
    print(cols_with_nas)
else:
    print("The dataset does not contain any NAs.")




#Exercise 06. Delete the NAs of the dataset, if applicable (★★☆)
#Print a comparison between the dimensions of the original DataFrame versus the DataFrame after the deletions.

import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Store original dimensions
original_shape = ds.shape

# Remove rows with NAs
ds_cleaned = ds.dropna()

# Store cleaned dimensions
cleaned_shape = ds_cleaned.shape

# Print comparison of dimensions
print(f"Original DataFrame dimensions: {original_shape}")
print(f"DataFrame dimensions after removing NAs: {cleaned_shape}")

# Check how many rows were removed
rows_removed = original_shape[0] - cleaned_shape[0]
print(f"Number of rows removed: {rows_removed}")



#Exercise 07. Which is the mean of prices in the population (level5 column) of "Arroyomolinos (Madrid)"? (★★☆)
#Print the obtained value.

import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Filter the dataset for the population "Arroyomolinos (Madrid)"
arroyomolinos_data = ds[ds['level5'] == 'Arroyomolinos (Madrid)']  # Assuming 'level5' is the population column

# Calculate the mean price
mean_price = arroyomolinos_data['price'].mean()  # Assuming 'price' is the price column

# Print the mean price
print(f"The mean price of houses in 'Arroyomolinos (Madrid)' is {mean_price:.2f} USD.")




#Exercise 08. Plot the histogram of prices for the population (level5 column) of "Arroyomolinos (Madrid)" and explain what you observe (★★☆)
#Print the histogram of the prices and write in the Markdown cell a brief analysis about the plot.


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Filter the dataset for the population "Arroyomolinos (Madrid)"
arroyomolinos_data = ds[ds['level5'] == 'Arroyomolinos (Madrid)']  # Assuming 'level5' is the population column

# Extract prices for the filtered population
prices = arroyomolinos_data['price']  # Assuming 'price' is the price column

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=10, color='skyblue', alpha=0.8, edgecolor='black')
plt.title("Histogram of Prices in 'Arroyomolinos (Madrid)'", fontsize=16)
plt.xlabel("Price (USD)", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
Observations and Analysis:
Price Distribution:

The histogram will show the spread of property prices 
in "Arroyomolinos (Madrid)." For example:
If the bars are concentrated around a specific range,
 it suggests most properties are priced similarly.
A wider spread indicates diverse pricing.
Peaks:

Peaks (tall bars) in the histogram represent price ranges 
with a high number of properties.
A peak at a lower price range might suggest affordability in that area.

Outliers:

If there are bars far away from the rest of the distribution,
 it may indicate outliers, such as luxury home
 
 
 
 #Exercise 09. Are the average prices of "Valdemorillo" and "Galapagar" the same? (★★☆)
#Print both average prices and then write a conclusion about them.
 
import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Filter data for "Valdemorillo" and "Galapagar"
valdemorillo_data = ds[ds['level5'] == 'Valdemorillo']  # Assuming 'level5' is the population column
galapagar_data = ds[ds['level5'] == 'Galapagar']

# Calculate the average prices
valdemorillo_avg_price = valdemorillo_data['price'].mean()  # Assuming 'price' is the price column
galapagar_avg_price = galapagar_data['price'].mean()

# Print the results
print(f"Average price in Valdemorillo: {valdemorillo_avg_price:.2f} USD")
print(f"Average price in Galapagar: {galapagar_avg_price:.2f} USD")

# Compare and conclude
if valdemorillo_avg_price == galapagar_avg_price:
    print("The average prices in Valdemorillo and Galapagar are the same.")
else:
    print("The average prices in Valdemorillo and Galapagar are different.")


#Exercise 10. Are the average prices per square meter (price/m2) of "Valdemorillo" and "Galapagar" the same? (★★☆)
#Print both average prices and then write a conclusion about it.

#Hint: Create a new column called pps (price per square meter) and 
#then analyze the values.

import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Create a new column for price per square meter (pps)
ds['pps'] = ds['price'] / ds['surface']  # Assuming 'price' and 'surface' columns exist

# Filter data for "Valdemorillo" and "Galapagar"
valdemorillo_data = ds[ds['level5'] == 'Valdemorillo']  # Assuming 'level5' is the population column
galapagar_data = ds[ds['level5'] == 'Galapagar']

# Calculate the average price per square meter for both populations
valdemorillo_avg_pps = valdemorillo_data['pps'].mean()
galapagar_avg_pps = galapagar_data['pps'].mean()

# Print the results
print(f"Average price per square meter in Valdemorillo: {valdemorillo_avg_pps:.2f} USD/m²")
print(f"Average price per square meter in Galapagar: {galapagar_avg_pps:.2f} USD/m²")

# Compare and conclude
if valdemorillo_avg_pps == galapagar_avg_pps:
    print("The average price per square meter in Valdemorillo and Galapagar is the same.")
else:
    print("The average price per square meter in Valdemorillo and Galapagar is different.")



#Exercise 11. Analyze the relation between the surface and the price of the houses (★★☆)
#Hint: You can make a scatter plot, then write a conclusion about it.

import matplotlib.pyplot as plt

# Scatter plot for surface vs. price
plt.figure(figsize=(10, 6))
plt.scatter(ds['surface'], ds['price'], alpha=0.7, c='blue', edgecolor='black')
plt.title("Scatter Plot: Surface vs. Price of Houses", fontsize=16)
plt.xlabel("Surface (m²)", fontsize=14)
plt.ylabel("Price (USD)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#then write a conclusion about it.
concluded that there is one property measuring 25e4 m2 at a very
affordable price 3.2e5 usd.
there are other two in this condition, but measure 6.67e4 at 4.4e5 usd.
which makes even more attypical the first conclusion.
the last outlier is at 1.68e4 m2 and 1.3e5 usd



#Exercise 12. How many real estate agencies does the dataset contain? (★★☆)
#Print the obtained value.


import pandas as pd

# Count the number of unique real estate agencies
unique_agencies = ds['realEstate_name'].nunique()  # 'realEstate_name' is the correct column for agency names

# Print the result
print(f"The dataset contains {unique_agencies} real estate agencies.")




#Exercise 13. Which is the population (level5 column) that contains
# the most houses? (★★☆)
#Print both the population and the number of houses.


import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Find the population with the most houses
population_with_most_houses = ds['level5'].value_counts().idxmax()  # Population with the most houses
number_of_houses = ds['level5'].value_counts().max()  # Number of houses in that population

# Print the result
print(f"The population with the most houses is '{population_with_most_houses}' with {number_of_houses} houses.")




#Exercise 14. Now let's work with the "south belt" of Madrid. Make a subset of the original DataFrame that contains the following populations (level5 column): "Fuenlabrada", "Leganés", "Getafe", "Alcorcón" (★★☆)
#Hint: Filter the original DataFrame using the column level5 and the function isin.



import pandas as pd

# Load the dataset
file_path = r'C:\Users\rober ugalde\Documents\real_estate.csv'
ds = pd.read_csv(file_path, sep=';')

# Define the "south belt" populations
south_belt_populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]

# Filter the DataFrame using the level5 column and isin
south_belt_df = ds[ds['level5'].isin(south_belt_populations)]

# Print the first few rows of the subset to verify
print(south_belt_df.head())

# Print the dimensions of the subset
print(f"The south belt DataFrame contains {south_belt_df.shape[0]} rows and {south_belt_df.shape[1]} columns.")



#Exercise 15. Make a bar plot of the median of the prices and explain what you observe (you must use the subset obtained in Exercise 14) (★★★)
#Print the bar of the median of the prices 
and write in the Markdown cell a brief analysis about the plot.


# Define the "south belt" populations
south_belt_populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]

# Filter the DataFrame using the level5 column and isin
south_belt_df = ds[ds['level5'].isin(south_belt_populations)]


# Calculate the median prices for each population in the south belt
median_prices = south_belt_df.groupby('level5')['price'].median()

# Plot the bar chart
plt.figure(figsize=(10, 6))
median_prices.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Median Prices in the South Belt of Madrid", fontsize=16)
plt.xlabel("Population", fontsize=14)
plt.ylabel("Median Price (USD)", fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()


and write in the Markdown cell a brief analysis about the plot.
# write about the plot:
    
    
    We can see that the Getafe Population is the Highest median price
    to up 2.859e5 usd.   Which is really much higher than its closest
    Median price at Alcorcon, way lower at 1.789e5.  or even Leganes,
    at 1.700e5.


#Exercise 16. Calculate the sample mean and variance of the variables: price, rooms, surface area and bathrooms (you must use the subset obtained in Exercise 14) (★★★)
#Print both values for each variable


# Define the "south belt" populations
south_belt_populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]

# Filter the DataFrame using the level5 column and isin
south_belt_df = ds[ds['level5'].isin(south_belt_populations)]

# Calculate the sample mean and variance for the specified variables
variables = ['price', 'rooms', 'surface', 'bathrooms']

# Compute the sample mean and variance
results = {}
for var in variables:
    mean = south_belt_df[var].mean()
    variance = south_belt_df[var].var()
    results[var] = {'mean': mean, 'variance': variance}

# Print the results
for var, stats in results.items():
    print(f"Variable: {var}")
    print(f"  Mean: {stats['mean']:.2f}")
    print(f"  Variance: {stats['variance']:.2f}\n")




#Exercise 17. What is the most expensive house in each population? You must use the subset obtained in Exercise 14 (★★☆)
#Print both the address and the price of the selected house of each population. You can print a DataFrame or a single line for each population.


# Find the most expensive house in each population
most_expensive_houses = south_belt_df.loc[south_belt_df.groupby('level5')['price'].idxmax()]

# Select relevant columns to display
result = most_expensive_houses[['level5', 'address', 'price']]

# Print the results as a DataFrame
print(result)

# Print as individual lines
for _, row in result.iterrows():
    print(f"In {row['level5']}, the most expensive house is located at {row['address']} with a price of {row['price']} USD.")




#Exercise 18. Normalize the variable of prices for each population and 
#plot the 4 histograms in the same plot (you must use the subset obtained in Exercise 14) (★★★)
#For the normalization method, you can use the one you consider; 
there is not a single correct answer to this question. 
Print the plot and write in the Markdown cell a 
brief analysis about the plot.





import matplotlib.pyplot as plt

# Normalize the prices for each population
south_belt_df['normalized_price'] = south_belt_df.groupby('level5')['price'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Prepare the data for plotting
populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]
colors = ['blue', 'green', 'orange', 'red']
plt.figure(figsize=(10, 6))

# Plot histograms for each population
for population, color in zip(populations, colors):
    subset = south_belt_df[south_belt_df['level5'] == population]
    plt.hist(
        subset['normalized_price'],
        bins=10,
        alpha=0.5,
        label=population,
        color=color,
        edgecolor='black'
    )

# Customize the plot
plt.title("Normalized Price Histograms for the South Belt of Madrid", fontsize=16)
plt.xlabel("Normalized Price", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.legend(title="Population")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()


#Print the plot and write in the Markdown cell a 
#brief analysis about the plot.

Leganés and Alcorcón exhibit more consistent pricing patterns.
Fuenlabrada and Getafe show greater variability, likely reflecting a mix of affordable and higher-priced houses.
Spread:

Some populations (e.g., Getafe) have a wider spread, indicating more variability in housing prices.
Other populations (e.g., Alcorcón) appear more compact, suggesting a more uniform pricing structure.

Outliers:

The presence of bars extending far to the right (e.g., near 4 or 5) may indicate extremely expensive houses relative to the population average.




# Exercise 19. What can you say about the price per square meter (price/m2) between the towns of "Getafe" and "Alcorcón"? You must use the subset obtained in Exercise 14 (★★☆)
#Hint: Create a new column called pps (price per square meter) and then analyze the values.


# Create a new column for price per square meter (pps)
south_belt_df['pps'] = south_belt_df['price'] / south_belt_df['surface']

# Filter data for "Getafe" and "Alcorcón"
getafe_data = south_belt_df[south_belt_df['level5'] == 'Getafe']
alcorcon_data = south_belt_df[south_belt_df['level5'] == 'Alcorcón']

# Calculate summary statistics for price per square meter (pps)
getafe_pps_mean = getafe_data['pps'].mean()
getafe_pps_median = getafe_data['pps'].median()
alcorcon_pps_mean = alcorcon_data['pps'].mean()
alcorcon_pps_median = alcorcon_data['pps'].median()

# Print the results
print(f"Getafe: Mean PPS = {getafe_pps_mean:.2f}, Median PPS = {getafe_pps_median:.2f}")
print(f"Alcorcón: Mean PPS = {alcorcon_pps_mean:.2f}, Median PPS = {alcorcon_pps_median:.2f}")

# Plot histograms for PPS comparison
plt.figure(figsize=(10, 6))
plt.hist(getafe_data['pps'], bins=10, alpha=0.5, label='Getafe', color='blue', edgecolor='black')
plt.hist(alcorcon_data['pps'], bins=10, alpha=0.5, label='Alcorcón', color='orange', edgecolor='black')
plt.title("Comparison of Price per Square Meter (PPS) Between Getafe and Alcorcón", fontsize=16)
plt.xlabel("Price per Square Meter (USD/m²)", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.legend(title="Population")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()

#what can I say


The Getafe PPSQM HITS a max at 81 units with average PPSQM 1913 usd/m2



#Exercise 20. Make the same plot for 4 different populations (level5 column) 
#and rearrange them on the same graph. You must use the subset obtained in Exercise 14 (★★☆)
#Hint: Make a scatter plot of each population using subplots.


# Define the populations to plot
populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]

# Create a figure with subplots for each population
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

# Scatter plot for each population
for i, population in enumerate(populations):
    subset = south_belt_df[south_belt_df['level5'] == population]
    axes[i].scatter(subset['surface'], subset['price'], alpha=0.7, edgecolor='black', label=population)
    axes[i].set_title(f"{population}", fontsize=14)
    axes[i].set_xlabel("Surface (m²)", fontsize=12)
    axes[i].set_ylabel("Price (USD)", fontsize=12)
    axes[i].grid(True, linestyle='--', alpha=0.7)
    axes[i].legend()

# Adjust layout
plt.tight_layout()
plt.suptitle("Scatter Plots of Surface vs Price for South Belt Populations", fontsize=16, y=1.02)

# Show the plot
plt.show()



#Exercise 21. Make a plot of the coordinates (latitude and longitude columns) of the south belt of Madrid by color of each population (you must use the subset obtained in Exercise 14) (★★★★)
#Execute the following cell, and then start coding in the next one. You must implement a simple code that transforms the coordinates columns in a Python dictionary (add more information if needed) and then add it to the map



from ipyleaflet import Map, basemaps

# Map centered on (60 degrees latitude and -2.2 degrees longitude)
# Latitude, longitude
map = Map(center = (60, -2.2), zoom = 2, min_zoom = 1, max_zoom = 20, 
    basemap=basemaps.Stamen.Terrain)
map
## HERE: plot the coordinates of the estates

from ipyleaflet import Map, Marker, basemaps, Icon

# Map centered on the south belt of Madrid
map = Map(center=(40.35, -3.75), zoom=12, basemap=basemaps.Stamen.Terrain)

# Define colors for each population
population_colors = {
    "Fuenlabrada": "blue",
    "Leganés": "green",
    "Getafe": "orange",
    "Alcorcón": "red"
}

# Add markers for each estate in the subset
for _, row in south_belt_df.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    population = row['level5']
    color = population_colors.get(population, "black")  # Default to black if population not found

    # Create and add a marker
    marker = Marker(location=(latitude, longitude), icon=Icon(color=color), draggable=False)
    map.add_layer(marker)

# Display the map
map



or: 

import pandas as pd

# This CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('C:/Users/rober ugalde/Documents/real_estate.csv', sep=';')
ds





#pip install folium

import folium

# Define the populations in the south belt
south_belt_populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]

# Filter the original DataFrame (assuming the original DataFrame is named 'ds')
south_belt_df = ds[ds['level5'].isin(south_belt_populations)]




# Create the base map centered on the south belt of Madrid
map_center = [40.35, -3.75]  # Approximate center of the south belt of Madrid
m = folium.Map(location=map_center, zoom_start=12)

# Define colors for each population
population_colors = {
    "Fuenlabrada": "blue",
    "Leganés": "green",
    "Getafe": "orange",
    "Alcorcón": "red"
}

# Add markers for each estate in the subset
for _, row in south_belt_df.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    population = row['level5']
    color = population_colors.get(population, "black")  # Default to black if population not found

    # Add a marker to the map
    folium.Marker(
        location=[latitude, longitude],
        popup=f"{population}",
        icon=folium.Icon(color=color)
    ).add_to(m)

# Display the map
m.save('south_belt_map.html')
print("Map saved as 'south_belt_map.html'. Open this file in your browser to view the map.")
