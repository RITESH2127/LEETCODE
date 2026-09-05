# Write your MySQL query statement below
WITH ReportStats AS (
    SELECT 
        reports_to, 
        COUNT(employee_id) AS reports_count, 
        ROUND(AVG(age)) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)
SELECT 
    e.employee_id, 
    e.name, 
    r.reports_count, 
    r.average_age
FROM Employees e
INNER JOIN ReportStats r 
    ON e.employee_id = r.reports_to
ORDER BY 
    e.employee_id;