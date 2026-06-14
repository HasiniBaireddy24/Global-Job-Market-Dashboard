import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

countries = ["in", "sg", "us", "gb", "ca", "au"]

roles = [
    "Data Analyst",
    "Business Analyst",
    "BI Analyst",
    "Product Analyst",
    "Data Scientist"
]

all_jobs = []

for country in countries:
    for role in roles:
        for page in range(1, 4):  # 3 pages

            print(f"Collecting {role} | {country} | Page {page}")

            url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"

            params = {
                "app_id": APP_ID,
                "app_key": APP_KEY,
                "what": role,
                "results_per_page": 20
            }

            response = requests.get(url, params=params)

            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                continue

            jobs = response.json().get("results", [])

            for job in jobs:

                all_jobs.append({
                    "job_id": job.get("id"),
                    "title": job.get("title"),
                    "company": job.get("company", {}).get("display_name"),
                    "location": job.get("location", {}).get("display_name"),
                    "salary_min": job.get("salary_min"),
                    "salary_max": job.get("salary_max"),
                    "created": job.get("created"),
                    "category": job.get("category", {}).get("label"),
                    "description": job.get("description"),
                    "url": job.get("redirect_url"),
                    "country": country,
                    "role_searched": role
                })

df = pd.DataFrame(all_jobs)

df.drop_duplicates(subset=["job_id"], inplace=True)

print(f"\nTotal Jobs Collected: {len(df)}")

df.to_csv("data/raw/global_jobs_raw.csv", index=False)

print("Dataset saved successfully!")