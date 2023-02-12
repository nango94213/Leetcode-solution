# Write your MySQL query statement below
WITH recursive numbers AS (SELECT 1 AS num UNION ALL SELECT num + 1 FROM numbers WHERE num < (select max(customer_id) from Customers))
  
select num ids from numbers where num not in (select customer_id from Customers)