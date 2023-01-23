# Write your MySQL query statement below

with cte as(select * from Logins),

cte2 as(select distinct *, dense_rank() over(partition by id order by login_date asc) rn from cte),

cte3 as(select id, DATEDIFF(login_date, CURDATE()) - cast(rn as signed) diff, count(*) total from cte2 group by id, diff order by id, login_date asc)

select distinct a.id, a.name from Accounts a join cte3 b on a.id = b.id where total >= 5 order by id asc




