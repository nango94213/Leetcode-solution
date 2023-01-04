# Write your MySQL query statement below


select if (from_id < to_id, from_id, to_id) person1, if (from_id < to_id, to_id, from_id) person2, count(duration) call_count, sum(duration) total_duration from Calls group by person1, person2