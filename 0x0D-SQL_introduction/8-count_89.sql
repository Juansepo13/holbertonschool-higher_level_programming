-- Displays the number of records with id = 89 in first_table of a database.
-- Syntax: SELECT [FROM table_references] [WHERE where_condition].
-- COUNT(*) returns a count of the number of rows retrieved, whether or not they contain NULL values.
SELECT COUNT(id) FROM first_table WHERE id=89;
