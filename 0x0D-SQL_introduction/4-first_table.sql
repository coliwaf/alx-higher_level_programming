-- Creates "first_table" table in current database in the server
-- If exists script shouldn't fail, Can't use SELECT and SHOW
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
