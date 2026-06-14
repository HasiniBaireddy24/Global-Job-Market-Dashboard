import pandas as pd
import re

# Load prepared dataset
df = pd.read_csv("data/cleaned/global_jobs_prepared.csv")

# List of skills to extract
skills = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "aws",
    "azure",
    "machine learning",
    "pandas",
    "numpy",
    "statistics",
    "r",
    "spark",
    "pyspark",
    "mysql",
    "postgresql",
    "google sheets",
    "data modeling",
    "data visualization",
    "big data",
    "etl",
    "data pipeline"
]

# Convert descriptions to lowercase
df["description_lower"] = df["description"].str.lower()

# Create skill columns
for skill in skills:

    # Special handling for R
    if skill == "r":
        pattern = r"\br\b"

    # Escape special characters for all other skills
    else:
        pattern = re.escape(skill)

    df[skill] = (
        df["description_lower"]
        .str.contains(pattern, regex=True, na=False)
        .astype(int)
    )

# Remove temporary column
df.drop(columns=["description_lower"], inplace=True)

# Save enhanced dataset
output_path = "data/cleaned/global_jobs_skills.csv"
df.to_csv(output_path, index=False)

# Print skill frequencies
print("\nTop Skills:\n")
print(df[skills].sum().sort_values(ascending=False))

print(f"\nDataset saved to: {output_path}")
print(f"Total Jobs: {len(df)}")