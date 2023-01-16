# Write your MySQL query statement below

with cte as(select a.user_id user1_id, b.user_id user2_id, rank() over(order by count(*) desc) rk from Relations a join Relations b on a.user_id < b.user_id and a.follower_id = b.follower_id group by a.user_id, b.user_id)

select user1_id, user2_id from cte where rk = 1
