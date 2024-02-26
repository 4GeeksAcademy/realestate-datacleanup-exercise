#### Exercise 06. Delete the NAs of the dataset, if applicable (★★☆)

#Print a comparison between the dimensions of the original DataFrame versus the DataFrame after the deletions

import pandas as pd

# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')

# Get the dimensions of the original dataset
dimension = ds.info()
#print(dimension)

# Delete the NA's

clean_df = ds.dropna()
clean_dimension = clean_df.info()

print(clean_dimension)

## Solution: It seems is empty after deleting the NA's ??

