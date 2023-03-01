# Write your MySQL query statement below

with cte as(select b.page_id from Friendship a join Likes b on if(a.user2_id = 1, a.user1_id, a.user2_id) = b.user_id where a.user1_id = 1 or a.user2_id = 1)

select distinct page_id recommended_page from cte where page_id not in (select page_id from Likes where user_id = 1)