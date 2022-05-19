-- script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- display both the score and the name (in this order)
-- Lists all records with a score >= 10 in the table second_table.
-- SELECT is used to retrieve rows selected from one or more tables.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC, name;
