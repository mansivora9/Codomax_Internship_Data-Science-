import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df =pd.read_csv("data.csv")
print(df)

# remove extra spaces from column names
df.columns = df.columns.str.strip()

# line chart
plt.figure(figsize=(10,5))
plt.plot(df["student_id"], df["age"], marker='o')
plt.title("Student id vs Age")
plt.xlabel("Student ID")
plt.ylabel("Age")
plt.grid(True)
plt.show()

# Bar chart
department_count = df['department'].value_counts()

plt.figure(figsize=(10,5))
plt.bar(department_count.index, department_count.values)
plt.title("Number of students in each department")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.xticks(rotation=45)
plt.show()

# pie chart
gender_count = df["gender"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    gender_count.values,
    labels=gender_count.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Gender Distribution")
plt.show()

