# Write your MySQL query statement below
SELECT employee_id,
IF(employee_id % 2 <>0 and name not like 'M%' , salary,0) as bonus 
From Employees Order By employee_id