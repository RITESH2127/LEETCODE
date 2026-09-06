# Write your MySQL query statement below
SELECT 
    employee_id, 
    department_id
FROM (
    SELECT 
        employee_id,
        department_id,
        primary_flag,
        COUNT(department_id) OVER(PARTITION BY employee_id) AS dept_count
    FROM 
        Employee
) sub
WHERE 
    primary_flag = 'Y' 
    OR dept_count = 1;