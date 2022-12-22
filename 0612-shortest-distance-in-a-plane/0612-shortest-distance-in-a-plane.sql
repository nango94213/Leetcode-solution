# Write your MySQL query statement below

#select min(sqrt(power(t2.x-t1.x, 2)+power(t2.y-t1.y,2))) from Point2D t1, Point2D t2 where t1.x != t2.x and t1.y != t2.y
with etc as(select *, row_number() over() number from Point2D)

select round(min(sqrt(power(t2.x-t1.x, 2)+power(t2.y-t1.y,2))), 2) shortest from etc t1, etc t2 where t1.number != t2.number