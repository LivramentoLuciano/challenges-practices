-- Write an SQL query to report the second highest salary from the Employee table.
-- If there is no second highest salary, the query should report null.
--
-- Table: Employee
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key column for this table.
-- Each row of this table contains information about the salary of an employee.
--
-- The query result format is in the following example.
-- Example 1:
-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+
--
-- Example 2:
-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | null                |
-- +---------------------+
-- 
-- Solución:
-- * Falla cuando NO hay 2do maximo salario (da vacío, pero se pidió NULL)
-- SELECT DISTINCT salary AS SecondHighestSalary
-- FROM Employee
-- ORDER BY salary DESC
-- LIMIT 1 OFFSET 1
--
-- Si englobamos el anterior en un SELECT, arrojará NULL
-- cuando el interior sea una tabla vacía
SELECT (
    SELECT DISTINCT salary 
    FROM Employee 
    ORDER BY Salary DESC 
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary

-- Esta opción es más clara y devuelve NULL si no existe
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)
