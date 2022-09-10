class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #space optimised
        n,buy,sell= len(prices), -prices[0], 0
        for i in range(1,n):
            buy,sell=max(-prices[i]+sell,buy),max(prices[i]+buy,sell)
        return sell
        