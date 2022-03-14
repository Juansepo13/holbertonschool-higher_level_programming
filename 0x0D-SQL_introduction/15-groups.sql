-- Lists the number of records with the same score a the table.
-- SELECT is used to retrieve rows selected from one or more tables.
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
