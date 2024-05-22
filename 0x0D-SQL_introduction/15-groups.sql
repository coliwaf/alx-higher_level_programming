-- Lists the number of records with the same score in the table 'second_table'
SELECT `score`, COUNT(`score`) AS `number` FROM `second_table` GROUP_BY `score` ORDER_BY `score` DESC;
