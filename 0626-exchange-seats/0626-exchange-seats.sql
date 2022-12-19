# Write your MySQL query statement below
select a.id, case
when mod(a.id, 2) = 0 then c.student
when mod(a.id, 2) != 0 and b.student is not null then b.student
else a.student
end student
from Seat a left join Seat b on a.id = b.id - 1 left join Seat c on a.id = c.id + 1 
