# Write your MySQL query statement below

with cte as(select m.member_id, m.name, case when count(v.visit_id) = 0 then -1 else (100*count(p.charged_amount)) / count(v.visit_id) end info from Members m left join Visits v on m.member_id = v.member_id left join Purchases p on v.visit_id = p.visit_id group by m.member_id)

select member_id, name, case when info = -1 then 'Bronze' when info < 50 then 'Silver' when info < 80 then 'Gold' else 'Diamond' end category from cte