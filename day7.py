import pandas as pd
df = pd.read_csv("data.csv")
print(df)

# remove extra spaces from column names
df.columns = df.columns.str.strip()
print(df)

#average age 
print("Average age")
print(df['age'].mean())

# maximum age
print("Maximum age")
print(df['age'].max())

# minimum age
print("Minimum age")
print(df['age'].min())  

# total students
print("Total students")
print(df['student_id'].count())

# student in each department
print("Student count in each department")
print(df['department'].value_counts())

# average age in each department
print("Average age in each department")
print(df.groupby('department')['age'].mean())   

# male and female count
print("Male and Female count")
print(df['gender'].value_counts())
