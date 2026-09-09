WITH LatestPrices AS (
    SELECT 
        product_id,
        new_price,
        ROW_NUMBER() OVER (
            PARTITION BY product_id 
            ORDER BY change_date DESC
        ) AS rn
    FROM 
        Products
    WHERE 
        change_date <= '2019-08-16'
),
UniqueProducts AS (
    SELECT DISTINCT 
        product_id 
    FROM 
        Products
)
SELECT 
    u.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM 
    UniqueProducts u
LEFT JOIN 
    LatestPrices lp 
    ON u.product_id = lp.product_id AND lp.rn = 1;