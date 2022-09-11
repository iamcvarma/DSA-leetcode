# Write your MySQL query statement below
select firstName,lastName, city,state from Person A Left JOIN Address B on A.personId = B.personId 