class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def solve(i,buy):
            if i==n:return 0
            k = (i,buy)
            if k in dp:return dp[k]
            if buy:
                dp[k] = max(-prices[i]+solve(i+1,0),solve(i+1,1))
            else:
                dp[k] = max(prices[i]-fee+solve(i+1,1),solve(i+1,0))
            return dp[k]
        n=len(prices)
        dp={}
        return solve(0,1)