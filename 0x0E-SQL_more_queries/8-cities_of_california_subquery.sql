-- Lists all the cities of California that can be found in the database hbtn_0d_usa.
-- ORDER BY keyword used to sort the result-set in ascending order.
SELECT c.id, c.name FROM cities AS c, states AS s WHERE c.state_id=s.id AND s.name = "California" ORDER BY c.id ASC;
