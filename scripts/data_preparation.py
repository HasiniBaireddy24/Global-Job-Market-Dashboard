import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned/global_jobs_cleaned.csv")

print("Original Shape:", df.shape)

# Convert created date
df["created"] = pd.to_datetime(df["created"])

# Fill missing companies
df["company"] = df["company"].fillna("Unknown")

# Create average salary
df["avg_salary"] = (
    df["salary_min"] + df["salary_max"]
) / 2

# Map country codes to names
country_map = {
    "in": "India",
    "sg": "Singapore",
    "us": "United States",
    "gb": "United Kingdom",
    "ca": "Canada",
    "au": "Australia"
}

df["country_name"] = df["country"].map(country_map)

# Extract year and month
df["year"] = df["created"].dt.year
df["month"] = df["created"].dt.month

print("\nPrepared Shape:", df.shape)

# Save prepared dataset
df.to_csv(
    "data/cleaned/global_jobs_prepared.csv",
    index=False
)

print("Data preparation completed!")