-- A script that orders data from a table --
-- In Ascending order --
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
