-- Task: List all the number of records with the same score
SELECT COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
