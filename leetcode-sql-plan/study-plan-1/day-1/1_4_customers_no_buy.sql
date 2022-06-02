-- Write an SQL query to report all customers who never order anything.
-- Return the result table in any order.
-- The query result format is in the following example.
-- 
-- Customers:
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
-- id is the primary key column for this table.
-- Each row of this table indicates the ID and name of a customer.
--
-- Orders
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | customerId  | int  |
-- +-------------+------+
-- id is the primary key column for this table.
-- customerId is a foreign key of the ID from the Customers table.
-- Each row of this table indicates the ID of an order and the ID of the customer who ordered it.


SELECT name AS Customers
FROM Customers 
WHERE id NOT IN (
    SELECT c.id
    FROM Orders AS o
    LEFT JOIN Customers AS c ON o.customerId = c.id
)
