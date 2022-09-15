# Write your MySQL query statement below
select stock_name,SUM(IF(operation="Buy",-price,price)) as capital_gain_loss
from Stocks
Group By stock_name