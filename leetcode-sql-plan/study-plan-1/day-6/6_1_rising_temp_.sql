-- Write an SQL query to find all dates' Id with 
-- higher temperatures compared to its previous dates (yesterday).
-- Return the result table in any order.
-- 
-- Table: Weather
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the primary key for this table.
-- This table contains information about the temperature on a certain day.
--
-- The query result format is in the following example.
-- Example 1:
-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
--
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation: 
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

-- Uso de LAG falla si los registros consecutivos no corresponden a dias consecutivos
-- SELECT (temperature - LAG(temperature) OVER(ORDER BY recordDate ASC)) AS dif_temp
-- FROM Weather

-- Solucion, comparando entre 2 tablas Weather en base a DATEDIFF (o INTERVAL 1 DAY),
-- los registros de dias consecutivos (si tienen o no temperatura superior)
SELECT w1.id
FROM Weather AS w1, Weather AS w2
WHERE w1.temperature > w2.temperature AND 
      DATEDIFF(w1.recordDate, w2.recordDate) = 1