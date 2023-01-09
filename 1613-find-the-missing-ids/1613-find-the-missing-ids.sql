# Write your MySQL query statement below
WITH RECURSIVE seq AS (
    SELECT 1 AS value UNION ALL SELECT value + 1 FROM seq WHERE value <= 100
    ),
cte as(select max(customer_id) mx from Customers)

SELECT value ids FROM seq, cte where value not in (select customer_id from Customers) and value <= mx