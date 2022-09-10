class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(i,buy):
            if i==n:return 0
            key = (i,buy)
            if key in dp:return dp[key]
            if buy:
                dp[key]=max(-prices[i]+solve(i+1,0),solve(i+1,1))
            else:
                dp[key]= max(prices[i]+solve(i+1,1),solve(i+1,0))
            return dp[key]
        n=len(prices)
        dp={}
        return solve(0,1)