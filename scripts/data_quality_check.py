import pandas as pd

# Load dataset
df = pd.read_csv("data/cleaned/global_jobs_cleaned.csv")

print("=" * 50)
print("DATA QUALITY REPORT")
print("=" * 50)

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Job IDs
print("\nDuplicate Job IDs:")
print(df["job_id"].duplicated().sum())

# Country distribution
print("\nCountry Distribution:")
print(df["country"].value_counts())

# Role Distribution
print("\nRole Distribution:")
print(df["role_searched"].value_counts())

# Missing descriptions
print("\nMissing Descriptions:")
print(df["description"].isnull().sum())

# Missing companies
print("\nMissing Companies:")
print(df["company"].isnull().sum())

# Missing locations
print("\nMissing Locations:")
print(df["location"].isnull().sum())

# Salary availability
print("\nSalary Min Available:")
print(df["salary_min"].notnull().sum())

print("\nSalary Max Available:")
print(df["salary_max"].notnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nQuality Check Completed!")

print("\nMissing Values Summary:")
print(df.isnull().sum())