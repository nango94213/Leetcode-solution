# Write your MySQL query statement below

select t1.id from Weather t1 where t1.temperature  > (select t2.temperature from Weather t2 where DATEDIFF(t1.recordDate, t2.recordDate) = 1);