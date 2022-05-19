-- Lists all records of a table with names in descending order.
-- SELECT is used to retrieve rows selected from one or more tables.
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
SELECT score,name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
