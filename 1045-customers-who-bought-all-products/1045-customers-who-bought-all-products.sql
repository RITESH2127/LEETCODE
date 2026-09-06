# Write your MySQL query statement below
WITH UniquePurchases AS (
    SELECT DISTINCT 
        customer_id, 
        product_key
    FROM 
        Customer
)
SELECT 
    customer_id
FROM 
    UniquePurchases
GROUP BY 
    customer_id
HAVING 
    COUNT(*) = (SELECT COUNT(*) FROM Product);