DELETE p1
FROM table p1
JOIN table p2
ON p1.duplicate_column = p2.duplicate_column
AND p1.id > p2.id;