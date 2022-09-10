class Solution:
    def maxProfit(self, cap: int, prices: List[int]) -> int:
        n,buy,sell=len(prices), [0]*(cap+1), [0]*(cap+1)
        for i in range(n-1,-1,-1):
            for k in range(1,cap+1):
                buy[k],sell[k]=max(-prices[i]+sell[k],buy[k]),max(prices[i]+buy[k-1],sell[k])
        return buy[cap]