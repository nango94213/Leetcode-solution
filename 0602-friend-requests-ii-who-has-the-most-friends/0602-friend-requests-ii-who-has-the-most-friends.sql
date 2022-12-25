# Write your MySQL query statement below

with cte as(select requester_id id from RequestAccepted union all select accepter_id from RequestAccepted),

cte2 as(select id, count(id) total from cte group by id)

select t.id, t.total num from (select *, rank() over(order by total desc) ranking from cte2) t where t.ranking = 1