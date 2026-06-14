import pandas as pd

df = pd.read_csv("data/cleaned/global_jobs_skills.csv")

# Keep only relevant columns
final_columns = [
    "job_id",
    "title",
    "company",
    "location",
    "country_name",
    "role_searched",
    "avg_salary",
    "created",

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

df = df[final_columns]

df.to_csv(
    "data/final/job_market_dashboard_dataset.csv",
    index=False
)

print("Final dashboard dataset created!")
print("Rows:", len(df))
print("Columns:", len(df.columns))