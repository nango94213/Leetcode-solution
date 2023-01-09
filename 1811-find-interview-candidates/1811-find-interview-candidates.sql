# Write your MySQL query statement below

with cte as(select u.name, u.mail from Contests c join Users u on c.gold_medal = u.user_id group by c.gold_medal having count(*) >= 3),

cte2 as(select gold_medal g0, silver_medal s0, bronze_medal b0, lag(gold_medal, 1) over(order by contest_id asc) g1, lag(silver_medal, 1) over(order by contest_id asc) s1, lag(bronze_medal, 1) over(order by contest_id asc) b1, lag(gold_medal, 2) over(order by contest_id asc) g2, lag(silver_medal, 2) over(order by contest_id asc) s2, lag(bronze_medal, 2) over(order by contest_id asc) b2 from Contests),

cte3 as (select u.name, u.mail from cte2 c join Users u on u.user_id in (g0, s0, b0) and u.user_id in (g1, s1, b1) and u.user_id in (g2, s2, b2))

select name, mail from cte union select name, mail from cte3