import pandas as pd

df = pd.read_csv("data/cleaned/global_jobs_skills.csv")

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

results = []

for role in df["role_searched"].unique():
    role_df = df[df["role_searched"] == role]

    for skill in skills:
        results.append({
            "Role": role,
            "Skill": skill,
            "Demand": role_df[skill].sum()
        })

summary = pd.DataFrame(results)

summary.to_csv(
    "data/final/role_skill_summary.csv",
    index=False
)

print(summary.head())
print("\nDataset created successfully!")