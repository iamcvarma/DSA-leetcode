class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #space optimised
        n,buy,sell=len(prices), 0, 0
        for i in range(n-1,-1,-1):
            buy,sell = max(-prices[i]+sell,buy),max(prices[i]-fee+buy,sell)
        return buy
        
        