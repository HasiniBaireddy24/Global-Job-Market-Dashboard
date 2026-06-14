import pandas as pd

df = pd.read_csv("data/cleaned/global_jobs_skills.csv")

print("\nJobs by Role:\n")
print(df["role_searched"].value_counts())

print("\nJobs by Country:\n")
print(df["country_name"].value_counts())

print("\nTop 10 Hiring Companies:\n")
print(df["company"].value_counts().head(10))

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

print("\nTop Skills:\n")
print(df[skills].sum().sort_values(ascending=False))


skills = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "aws",
    "azure",
    "machine learning"
]

print("\nSkill Demand by Role:\n")

for skill in skills:
    print(f"\n{skill.upper()}")
    print(
        df.groupby("role_searched")[skill]
        .sum()
        .sort_values(ascending=False)
    )


df["avg_salary"] = (
    df["salary_min"] + df["salary_max"]
) / 2

print("\nAverage Salary by Role:\n")
print(
    df.groupby("role_searched")["avg_salary"]
    .mean()
    .sort_values(ascending=False)
)


print("\nSalary Records by Role:\n")

print(
    df.groupby("role_searched")["avg_salary"]
    .count()
    .sort_values(ascending=False)
)

print("\nAverage Salary by Country:\n")

print(
    df.groupby("country_name")["avg_salary"]
    .mean()
    .sort_values(ascending=False)
)