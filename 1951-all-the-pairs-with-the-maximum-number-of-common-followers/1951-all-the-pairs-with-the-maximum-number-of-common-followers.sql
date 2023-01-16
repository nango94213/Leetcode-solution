# Write your MySQL query statement below

with cte as(select a.user_id user1_id, b.user_id user2_id, count(*) ct from Relations a join Relations b on a.user_id < b.user_id and a.follower_id = b.follower_id group by a.user_id, b.user_id)

select user1_id, user2_id from (select *, rank() over(order by ct desc) rk from cte) gg where gg.rk = 1