# Write your MySQL query statement below
select a.left_operand, a.operator, a.right_operand, case when a.operator = '=' then if(b.value = c.value, 'true', 'false') when a.operator = '>' then if(b.value > c.value, 'true', 'false') when a.operator = '<' then if(b.value < c.value, 'true', 'false') end value from Expressions a join Variables b on a.left_operand = b.name join Variables c on a.right_operand = c.name