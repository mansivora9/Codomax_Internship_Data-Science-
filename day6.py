import pandas as pd

# load dataset
df = pd.read_csv("data.csv")
print("Original dataset")
print(df.columns)
print(df.columns.tolist())

# select specific column
print("\nName and Age")
print(df[["name","age"]])

# filter rows
print("\nStudents with age > 25")
print(df[df["age"] > 25])

# sort data
print("\nSorted by Age")
print(df.sort_values(by="age", ascending=False))

# find unique values
print("\nUnique Departments")
print(df["department"].unique())

# count values
print("\nDepartment-wise Student Count")
print(df["department"].value_counts())
