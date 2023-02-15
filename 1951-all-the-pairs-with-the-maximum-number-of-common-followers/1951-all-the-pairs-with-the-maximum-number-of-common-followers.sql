# Write your MySQL query statement below

select ad user1_id, bd user2_id from (select a.user_id ad, b.user_id bd, rank() over(order by count(*) desc) total from Relations a join Relations b on a.follower_id = b.follower_id and a.user_id != b.user_id where a.user_id < b.user_id group by ad, bd) t where total = 1