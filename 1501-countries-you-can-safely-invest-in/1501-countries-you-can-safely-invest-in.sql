# Write your MySQL query statement below

select c.name country from Person p join Country c on c.country_code = SUBSTRING(p.phone_number, 1, 3) join Calls ca on p.id = ca.caller_id or p.id = ca.callee_id group by c.name having avg(ca.duration) > (select avg(duration) from Calls)