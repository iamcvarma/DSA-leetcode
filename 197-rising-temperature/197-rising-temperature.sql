# Write your MySQL query statement below

select A.id from Weather A,Weather B
where A.temperature > B.temperature AND TO_Days(A.recordDate)-To_days(B.recordDate)=1