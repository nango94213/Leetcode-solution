# Write your MySQL query statement below
/*select a.id, case
when mod(a.id, 2) = 0 then c.student
when mod(a.id, 2) != 0 and b.student is not null then b.student
else a.student
end student
from Seat a left join Seat b on a.id = b.id - 1 left join Seat c on a.id = c.id + 1 */

select case
when mod(id, 2) != 0 and id != last_one then id + 1
when mod(id, 2) = 0 then id - 1
else id
end as id,
student from seat, (select count(*) as last_one from Seat) t order by id