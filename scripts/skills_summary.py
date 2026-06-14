import pandas as pd

df = pd.read_csv("data/cleaned/global_jobs_skills.csv")

skills = [
    "python", "sql", "excel", "power bi", "tableau",
    "aws", "azure", "machine learning", "pandas",
    "numpy", "statistics", "r", "spark", "pyspark",
    "mysql", "postgresql", "google sheets",
    "data modeling", "data visualization",
    "big data", "etl", "data pipeline"
]

skill_counts = []

for skill in skills:
    skill_counts.append({
        "Skill": skill,
        "Demand": df[skill].sum()
    })

skills_df = pd.DataFrame(skill_counts)
skills_df = skills_df.sort_values("Demand", ascending=False)

skills_df.to_csv(
    "data/final/skills_summary.csv",
    index=False
)

print(skills_df.head(10))