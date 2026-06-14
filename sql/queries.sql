#Total Jobs
SELECT COUNT(*) AS total_jobs
FROM jobs;

#Jobs by country
SELECT country_name,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY country_name
ORDER BY total_jobs DESC;

#Jobs by role
SELECT role_searched,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY role_searched
ORDER BY total_jobs DESC;


#Top Hiring Companies
SELECT company,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY company
ORDER BY total_jobs DESC
LIMIT 10;


#Average salary by role
SELECT role_searched,
       ROUND(AVG(avg_salary),2) AS avg_salary
FROM jobs
GROUP BY role_searched
ORDER BY avg_salary DESC;