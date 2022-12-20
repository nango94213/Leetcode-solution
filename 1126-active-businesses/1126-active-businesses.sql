# Write your MySQL query statement below

select gg.business_id from (select e.business_id, sum(case when e.occurences > t.avg_act then 1 else 0 end) valid from Events e join (select event_type, avg(occurences) avg_act from Events group by event_type) t on e.event_type = t.event_type group by e.business_id) gg where gg.valid > 1
