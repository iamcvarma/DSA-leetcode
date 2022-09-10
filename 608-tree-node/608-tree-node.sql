# Write your MySQL query statement below
select id,IF(p_id is NULL,"Root",IF(id in (select p_id From Tree),"Inner","Leaf")) as type
From Tree
Order BY id