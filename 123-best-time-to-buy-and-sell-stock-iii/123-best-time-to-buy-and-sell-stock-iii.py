class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell=[0]*3,[0]*3
        for i in range(len(prices)-1,-1,-1):
            for k in (1,2):
                buy[k],sell[k]=max(-prices[i]+sell[k],buy[k]),max(prices[i]+buy[k-1],sell[k])               
        return buy[2]