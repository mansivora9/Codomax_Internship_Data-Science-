# importing pandas
import pandas as pd
print("Pandas imported successfully")

# load dataset
df = pd.read_csv("data.csv")

print(df)

# displaying first 5 rows of the dataset
print(df.head())

# displaying last 5 rows of the dataset
print(df.tail())

# displaying the shape of the dataset
print("Shape of the dataset:", df.shape)

# displaying the column names of the dataset
print("Column names of the dataset:", df.columns)

# displaying the data types of the columns in the dataset
print("Data types of the columns in the dataset:", df.dtypes)

# dataset information
print("Dataset Information:")
print(df.info())

# displaying the summary statistics of the dataset
print("Summary statistics of the dataset:")
print(df.describe())

# checking for missing values in the dataset
print("Checking for missing values in the dataset:")
print(df.isnull().sum())
