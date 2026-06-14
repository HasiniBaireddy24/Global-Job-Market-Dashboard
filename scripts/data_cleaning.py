import pandas as pd

df = pd.read_csv("data/raw/global_jobs_raw.csv")

print("Original Shape:", df.shape)

# Remove duplicate jobs
df.drop_duplicates(subset=["job_id"], inplace=True)

# Convert date column
df["created"] = pd.to_datetime(df["created"])

# Remove rows with missing title
df.dropna(subset=["title"], inplace=True)

print("Cleaned Shape:", df.shape)

df.to_csv("data/cleaned/global_jobs_cleaned.csv", index=False)

print("Cleaned dataset saved!")