-- Lists all records of "second_table", with a score of 'score >= 10'
-- displaying columns in order of 'score' and 'name' and the
-- results ordered by 'score'(top first)
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY score DESC;
