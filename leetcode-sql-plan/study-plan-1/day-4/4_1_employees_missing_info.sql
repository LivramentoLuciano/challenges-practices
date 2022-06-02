-- Write an SQL query to report the IDs of all the employees with missing information. 
-- The information of an employee is missing if:
-- The employee's name is missing, or
-- The employee's salary is missing.
-- Return the result table ordered by employee_id in ascending order.
--
-- Table: Employees
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | employee_id | int     |
-- | name        | varchar |
-- +-------------+---------+
-- employee_id is the primary key for this table.
-- Each row of this table indicates the name of the employee whose ID is employee_id.
-- 
-- Table: Salaries
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | employee_id | int     |
-- | salary      | int     |
-- +-------------+---------+
-- employee_id is the primary key for this table.
-- Each row of this table indicates the salary of the employee whose ID is employee_id.
--
--
-- The query result format is in the following example.
-- Example 1:
-- Input: 
-- Employees table:
-- +-------------+----------+
-- | employee_id | name     |
-- +-------------+----------+
-- | 2           | Crew     |
-- | 4           | Haven    |
-- | 5           | Kristian |
-- +-------------+----------+
-- Salaries table:
-- +-------------+--------+
-- | employee_id | salary |
-- +-------------+--------+
-- | 5           | 76071  |
-- | 1           | 22517  |
-- | 4           | 63539  |
-- +-------------+--------+
-- Output: 
-- +-------------+
-- | employee_id |
-- +-------------+
-- | 1           |
-- | 2           |
-- +-------------+
-- Explanation: 
-- Employees 1, 2, 4, and 5 are working at this company.
-- The name of employee 1 is missing.
-- The salary of employee 2 is missing.

-- Solución
-- MySQL parece no tiene FULL JOIN (MySQL Server sí)
-- MySQL -> UNION de LEFT OUTER Y RIGHT OUTER
-- [https://stackoverflow.com/questions/4796872/how-can-i-do-a-full-outer-join-in-mysql]
--
-- LEFT OUTER
-- UNION
-- RIGHT OUTER
--
-- SELECT *
-- FROM Employees AS e
-- LEFT JOIN Salaries AS s ON e.employee_id = s.employee_id
-- UNION
-- SELECT *
-- FROM Employees AS e
-- RIGHT JOIN Salaries AS s ON e.employee_id = s.employee_id
--

SELECT employee_id
FROM (
    SELECT e.employee_id AS employee_id, e.name, s.salary AS salary
    FROM Employees AS e
    LEFT JOIN Salaries AS s ON e.employee_id = s.employee_id
    UNION
    SELECT s.employee_id AS employee_id, e.name, s.salary AS salary
    FROM Employees AS e
    RIGHT JOIN Salaries AS s ON e.employee_id = s.employee_id
) AS j
WHERE name IS NULL OR salary IS null
ORDER BY employee_id ASC
