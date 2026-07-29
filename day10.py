import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove duplicate rows
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Display cleaned dataset
print("Cleaned Dataset")
print(df)

# Export cleaned dataset
df.to_csv("cleaned__data.csv", index=False)

print("✅ Cleaned dataset exported successfully!")