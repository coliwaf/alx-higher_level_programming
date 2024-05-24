-- Creates "second_table" table in "hbtn_0c_0" database and then
-- insert multiple rows, should not fail if table already exists and 
-- not allowed to use SELECT or SHOW
CREATE TABLE IF NOT EXISTS `second_table` (`id` INT, `name` VARCHAR(256), `score` INT);
INSERT INTO `second_table`(`id`, `name`, `score`) VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
