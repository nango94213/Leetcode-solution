# Write your MySQL query statement below

select id, num from (select requester_id id, count(*) num, rank() over(order by count(*) desc) rk from (select requester_id, accepter_id from RequestAccepted union all select accepter_id, requester_id from RequestAccepted) a group by id) b where b.rk = 1