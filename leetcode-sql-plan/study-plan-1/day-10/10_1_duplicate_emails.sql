-- Write an SQL query to report all the duplicate emails.
-- Return the result table in any order.
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
-- The query result format is in the following example.
-- Example 1:
-- Input: 
-- Person table:
-- +----+---------+
-- | id | email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- Output: 
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- Explanation: a@b.com is repeated two times.

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1

-- Variante con JOIN
-- SELECT DISTINCT t1.Email
-- FROM Person t1
-- JOIN Person t2
-- ON t1.email = t2.email and t1.id <> t2.id