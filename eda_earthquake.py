import pandas as pd

file_path = 'database.csv'
df = pd.read_csv(file_path)

# Displays the first 5 rows of the dataframe, verifies the data is loaded correctly
# print(df.head())

# Gives a summary of the dataframe, including the number of rows, columns, data types, and count of non-null values
# print(df.info())

# Shows how many values are missing in each column
# print(df.isnull().sum())

# Drop columns with too many missing values
columns_to_drop = ['Magnitude Error', 'Magnitude Seismic Stations', 'Horizontal Distance', 'Horizontal Error']

# Removes the columns from the dataframe
df.drop(columns=columns_to_drop, inplace=True)

# Shows the rows, then columns of the dataframe after dropping the columns
#print(df.shape)

print(df['Depth Error'].describe())
print(df['Depth Seismic Stations'].describe())
print(df['Azimuthal Gap'].describe())
print(df['Root Mean Square'].describe())
