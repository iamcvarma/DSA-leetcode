class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0,0] for _ in range(n)]
        dp[0]=[-prices[0],0]
        for i in range(1,n):
            dp[i][0]=max(-prices[i]+dp[i-1][1],dp[i-1][0])
            dp[i][1]=max(prices[i]+dp[i-1][0],dp[i-1][1])
        return dp[-1][1]