# Write your MySQL query statement below

select s.salesperson_id, s.name, sum(case when ss.price is not null then ss.price else 0 end) total from Salesperson s left join Customer c on s.salesperson_id = c.salesperson_id left join Sales ss on c.customer_id = ss.customer_id group by s.salesperson_id