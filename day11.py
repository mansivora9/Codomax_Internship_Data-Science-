import pandas as pd
df = pd.read_csv("cleaned__data.csv")
df.columns = df.columns.str.strip()

# Dataset Overview
print("Total Students:", len(df))

# Gender Distribution
print("\nGender Distribution:")
print(df["gender"].value_counts())

# Department Distribution
print("\nDepartment Distribution:")
print(df["department"].value_counts())

# Average Age
print("\nAverage Age:", round(df["age"].mean(), 2))

# Youngest Student
print("\nYoungest Student:")
print(df[df["age"] == df["age"].min()][["name", "age"]])

# Oldest Student
print("\nOldest Student:")
print(df[df["age"] == df["age"].max()][["name", "age"]])