class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy,sell,pre_buy=0,0,0
        for i in range(n-1,-1,-1):
            buy,sell,pre_buy=max(-prices[i]+sell,buy),max(prices[i]+pre_buy,sell),buy
        return buy