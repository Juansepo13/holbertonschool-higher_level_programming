-- Creates the database hbtn_0d_2 and the user user_0d_2.
-- CREATE DATABASE statement creates a database with the given name.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- CREATE USER statement creates new MySQL accounts.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
SET PASSWORD FOR user_0d_2@localhost = 'user_0d_2_pwd';
-- GRANT statement assigns privileges and roles to MySQL user accounts and roles.
-- Syntax: GRANT priv_type [(column_list)] [, priv_type [(column_list)]].
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- FLUSH PRIVILEGES statement reloads privileges from the grant tables in mysql system schema.
FLUSH PRIVILEGES;
