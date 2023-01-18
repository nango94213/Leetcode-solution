# Write your MySQL query statement below

with a as(select distinct(customer_id) from Orders where product_name = 'A'),

b as(select distinct(customer_id) from Orders where product_name = 'B'),

c as(select distinct(customer_id) from Orders where product_name = 'C')

select a.customer_id, customer_name from a join customers on a.customer_id = Customers.customer_id where a .customer_id in (select * from b) and a.customer_id not in (select * from c)