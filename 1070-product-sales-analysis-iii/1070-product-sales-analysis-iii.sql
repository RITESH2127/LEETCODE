# Write your MySQL query statement below
WITH MinYearSales AS (
    SELECT 
        product_id, 
        year, 
        quantity, 
        price,
        MIN(year) OVER (PARTITION BY product_id) as min_year
    FROM Sales
)
SELECT product_id, year AS first_year, quantity, price
FROM MinYearSales
WHERE year = min_year