class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(i,buy):
            if i>=len(prices):return 0
            k=(i,buy)
            if k in dp:return dp[k]
            if buy:
                dp[k]=max(-prices[i]+solve(i+1,0),solve(i+1,1))
            else:
                dp[k]=max(prices[i]+solve(i+2,1),solve(i+1,0))
            return dp[k]
        dp={}
        return solve(0,1)