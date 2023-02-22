# Write your MySQL query statement below

select business_id from (select *, avg(occurences) over(partition by event_type) av from Events) t group by business_id having sum(occurences>av) > 1