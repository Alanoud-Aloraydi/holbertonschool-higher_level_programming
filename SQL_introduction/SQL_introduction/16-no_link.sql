-- Lists all records of the table second_table that have a name value.
-- Results display the score and the name, ordered by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
