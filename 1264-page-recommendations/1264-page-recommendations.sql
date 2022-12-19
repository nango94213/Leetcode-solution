# Write your MySQL query statement below

select distinct(tmd.recommended_page) from (select case
when exists (select page_id target from Likes where user_id = 1) and l.page_id in (select page_id target from Likes where user_id = 1) then null
else l.page_id
end
recommended_page from (select case 
when user1_id = 1 then user2_id
when user2_id = 1 then user1_id
end as real_id from Friendship) t join Likes l on t.real_id = l.user_id) tmd where tmd.recommended_page is not null
