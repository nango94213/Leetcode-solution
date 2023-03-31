# Write your MySQL query statement below

with cte as(select avg(duration) avg_du from Calls)



select c.name country from Person p join Country c on substring(p.phone_number, 1, 3) = c.country_code join Calls ca on p.id = ca.caller_id or p.id = ca.callee_id group by c.name having avg(duration) > (select * from cte)