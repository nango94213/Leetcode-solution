# Write your MySQL query statement below
with cte as(select user1_id, user2_id from Friendship union all select user2_id, user1_id from Friendship)


select f.user1_id, ff.user1_id user2_id, count(*) common_friend from cte f join cte ff on f.user1_id < ff.user1_id and f.user2_id = ff.user2_id group by f.user1_id, ff.user1_id having common_friend >= 3 and (f.user1_id, ff.user1_id) in (select * from Friendship)