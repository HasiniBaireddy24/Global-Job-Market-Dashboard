# Global Job Market Intelligence Dashboard

## Project Overview

The Global Job Market Intelligence Dashboard is an end-to-end data analytics project that analyzes job market trends using real-world job postings collected through the Adzuna API.

The project involves data collection, data cleaning, skill extraction, exploratory data analysis, SQLite database integration, and Power BI dashboard development.

The dashboard provides insights into:

* Job opportunities across countries
* Hiring trends across different analytics roles
* Most in-demand skills
* Role-specific skill requirements
* Salary trends
* Top hiring companies

---

## Objectives

* Collect real-world job market data using an API
* Clean and prepare the data for analysis
* Extract skills from job descriptions
* Analyze hiring trends across countries and roles
* Build an interactive Power BI dashboard
* Generate insights from the collected data

---

## Tech Stack

### Programming

* Python
* Pandas
* NumPy

### Data Collection

* Adzuna API
* Requests
* Python-dotenv

### Database

* SQLite
* SQLAlchemy

### Visualization

* Power BI

---

## Dataset Information

### Countries Covered

* India
* United States
* United Kingdom
* Canada
* Australia
* Singapore

### Roles Covered

* Data Analyst
* Business Analyst
* BI Analyst
* Product Analyst
* Data Scientist

### Dataset Size

* Total Job Postings: 1,680
* Countries: 6
* Companies: 900+
* Skills Tracked: 20+

---

## Project Workflow

1. Collected job postings using the Adzuna API.
2. Cleaned and validated the dataset.
3. Performed data quality checks.
4. Extracted skills from job descriptions using keyword matching.
5. Conducted exploratory data analysis (EDA).
6. Loaded the processed data into SQLite.
7. Created dashboard-ready datasets.
8. Built an interactive Power BI dashboard.

---

## Dashboard Pages

### 1. Overview

* Total Jobs
* Total Companies
* Total Countries
* Jobs by Country
* Jobs by Role

### 2. Skills Intelligence

* Most In-Demand Skills
* Skill Demand KPIs

### 3. Role Skill Analysis

* Skill Demand Across Roles
* Top Skills for Data Scientists
* Top Skills for BI Analysts

### 4. Salary Insights

* Salary Records Available
* Average Salary by Role
* Average Salary by Country

### 5. Hiring Landscape

* Top Hiring Companies
* Hiring Distribution by Country
* Hiring Distribution by Role

---

## Key Insights

* SQL was the most frequently requested skill across job postings.
* Data Scientist roles showed strong demand for Machine Learning and Python.
* BI Analyst roles showed strong demand for Power BI and SQL.
* The United States and United Kingdom recorded the highest number of job postings in the dataset.
* Data Analyst and Business Analyst were the most in-demand roles.
* Companies such as ITOL Recruit, Eliassen Group, and Targeted Talent posted the highest number of jobs in the dataset.

---

## Project Structure

Global-Job-Market-Intelligence-Dashboard

├── dashboard/

├── data/

├── screenshots/

├── scripts/

├── sql/

├── job_market.db

├── README.md

├── requirements.txt

└── .gitignore



