-- Lists all records in second_table by score and name(in this order),
-- only those with name column, and listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
