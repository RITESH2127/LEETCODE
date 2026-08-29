# Write your MySQL query statement below
WITH first_login AS (
    SELECT
        player_id,
        event_date,
        MIN(event_date) OVER (PARTITION BY player_id) AS first_date
    FROM Activity
)

SELECT ROUND(
    COUNT(DISTINCT CASE
        WHEN event_date = DATE_ADD(first_date, INTERVAL 1 DAY)
        THEN player_id
    END)
    / COUNT(DISTINCT player_id),
    2
) AS fraction
FROM first_login;