-- Write an SQL query to delete all the duplicate emails,
-- keeping only one unique email with the smallest id. 
-- Note that you are supposed to write a DELETE statement and not a SELECT one.
--
-- After running your script, the answer shown is the Person table. 
-- The driver will first compile and run your piece of code 
-- and then show the Person table. 
-- The final order of the Person table does not matter.
--
-- 
-- Table: Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
-- id is the primary key column for this table.
-- Each row of this table contains an email. The emails will not contain uppercase letters.
--
--
-- The query result format is in the following example.
-- Example 1:
-- Input: 
-- Person table:
-- +----+------------------+
-- | id | email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- 
-- Output: 
-- +----+------------------+
-- | id | email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+
-- Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.

-- Filtrando con una subquery de los id minimos correspondientes a cada email
-- Tengo que wrapearlo en un SELECT de mas, porque sino tira error de runtime (TODO: ver)
-- OJO: pedia usar delete no select (supongo que eso incluye la subquery)
-- Resultado: 656 ms, faster than 83.20% 
DELETE
FROM Person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT MIN(id) AS id, email
        FROM Person
        GROUP BY email
    ) AS minid
)

-- Eliminando tras unir tablas con Join (segun el matcheo de un campo)
-- Resultado: 779 ms, faster than 66.76% 
DELETE p1
FROM Person AS p1 INNER JOIN Person AS p2 
ON p1.email = p2.email AND p1.id > p2.id

-- Simil anterior pero con WHERE
-- Resultado: 1893 ms, faster than 5.00%
DELETE p1
FROM Person p1, Person p2 
WHERE p1.email = p2.email AND p1.id > p2.id


