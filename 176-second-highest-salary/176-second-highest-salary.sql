# Write your MySQL query statement below
SELECT(
    SELECT DISTINCT salary
    FROM Employee
    Order By salary DESC
    Limit 1 Offset 1
) as SecondHighestSalary 