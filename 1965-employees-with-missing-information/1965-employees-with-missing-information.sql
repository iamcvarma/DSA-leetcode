select employee_id from Employees where employee_id not in (select employee_id from Salaries)
UNION
select employee_id from Salaries where employee_id not in (select employee_id from Employees)
ORDER BY employee_id