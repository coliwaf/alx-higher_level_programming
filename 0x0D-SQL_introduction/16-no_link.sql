-- Lists the number of records with the same score in the table 'second_table'
-- Don't list records without a name value and list them in order of 
-- 'score' then 'name'
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
