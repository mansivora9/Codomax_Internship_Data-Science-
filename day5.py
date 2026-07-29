# clean dataset
# importing pandas
import pandas as pd
print("Pandas imported successfully")

# load dataset
df = pd.read_csv("data.csv")

# check missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# remove duplicate rows
df = df.drop_duplicates()
print("Dataset after removing duplicates:")
print(df)

# fill missing values 
df = df.fillna("Unknown")
print("Dataset after filling missing values:")
print(df)

# rename columns
df = df.rename(columns={"name": "student_name"})
print("Dataset after renaming columns:")
print(df)

print("Cleaned dataset:")
print(df)

# save cleaned dataset to a new CSV file
df.to_csv("cleaned_data.csv", index=False)

print("Cleaned dataset saved to cleaned_data.csv")