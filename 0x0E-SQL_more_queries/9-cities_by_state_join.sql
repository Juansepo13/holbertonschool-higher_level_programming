-- Lists all cities contained in the database hbtn_0d_usa.
-- LEFT JOIN: Table "states" is set to depend on table "cities".
SELECT c.id, c.name, s.name FROM cities AS c INNER JOIN states AS s WHERE c.state_id=s.id ORDER BY c.id ASC;
