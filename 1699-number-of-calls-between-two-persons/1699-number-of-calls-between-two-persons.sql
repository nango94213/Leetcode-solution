# Write your MySQL query statement below


select case when from_id < to_id then from_id else to_id end person1, case when from_id < to_id then to_id else from_id end person2, count(duration) call_count, sum(duration) total_duration from Calls group by person1, person2