# Write your MySQL query statement below
with cte as(select article_id, viewer_id, view_date from Views),

cte2 as(select * from cte union select * from cte),

cte3 as(select count(*) ct, viewer_id from cte2 group by view_date, viewer_id)

select distinct(viewer_id) id from cte3 where ct > 1 order by id asc