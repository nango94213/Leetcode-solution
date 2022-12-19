# Write your MySQL query statement below

select distinct(l.page_id) recommended_page from (select case 
when user1_id = 1 then user2_id
when user2_id = 1 then user1_id
end as real_id from Friendship) t join Likes l on t.real_id = l.user_id where l.page_id not in (select page_id from Likes where user_id = 1)