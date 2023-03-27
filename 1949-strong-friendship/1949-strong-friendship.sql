# Write your MySQL query statement below
with cte as(select * from Friendship union all select user2_id, user1_id from Friendship)

select a.user1_id user1_id, b.user1_id user2_id, count(*) common_friend from cte a join cte b on a.user2_id = b.user2_id where a.user1_id < b.user1_id group by user1_id, user2_id having common_friend >= 3 and (a.user1_id, b.user1_id) in (select * from Friendship)