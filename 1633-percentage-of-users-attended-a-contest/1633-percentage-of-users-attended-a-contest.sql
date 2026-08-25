# Write your MySQL query statement below
SELECT 
    r.contest_id, 
    ROUND(COUNT(r.user_id) * 100.0 / u.total, 2) AS percentage
FROM Register r
CROSS JOIN (SELECT COUNT(user_id) AS total FROM Users) u
GROUP BY r.contest_id, u.total
ORDER BY percentage DESC, r.contest_id ASC;