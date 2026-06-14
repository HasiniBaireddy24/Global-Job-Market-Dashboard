import pandas as pd
import sqlite3

df = pd.read_csv("data/cleaned/global_jobs_skills.csv")

conn = sqlite3.connect("job_market.db")

df.to_sql(
    "jobs",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully!")

