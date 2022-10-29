-- Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
-- The test cases are generated so that exactly one customer will have placed more orders than any other customer.
--
-- Table: Orders
-- +-----------------+----------+
-- | Column Name     | Type     |
-- +-----------------+----------+
-- | order_number    | int      |
-- | customer_number | int      |
-- +-----------------+----------+
-- order_number is the primary key for this table.
-- This table contains information about the order ID and the customer ID.
--
-- The query result format is in the following example.
-- Example 1:
-- Input: 
-- Orders table:
-- +--------------+-----------------+
-- | order_number | customer_number |
-- +--------------+-----------------+
-- | 1            | 1               |
-- | 2            | 2               |
-- | 3            | 3               |
-- | 4            | 3               |
-- +--------------+-----------------+
-- Output: 
-- +-----------------+
-- | customer_number |
-- +-----------------+
-- | 3               |
-- +-----------------+
-- Explanation: 
-- The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
-- So the result is customer_number 3.
--
-- Follow up: What if more than one customer has the largest number of orders, 
-- can you find all the customer_number in this case?

-- Solución simple, un único cliente con mayor cantidad de ordenes
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1

-- Solución para caso en que haya más de un cliente con el mismo número de mayor cantidad de ordenes
-- Primero, identifico el valor de dicha maxima cantidad de ordenes
WITH MaxOrders AS (
    SELECT COUNT(*) AS customer_total_orders
    FROM Orders
    GROUP BY customer_number
    ORDER BY customer_total_orders DESC
    LIMIT 1
)

SELECT customer_number
FROM Orders
GROUP BY customer_number
HAVING COUNT(order_number) = (
    SELECT customer_total_orders 
    FROM MaxOrders
)