class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0]*(2) for _ in range(3)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for k in (1,2):
                dp[i][k][1]=max(-prices[i]+dp[i+1][k][0],dp[i+1][k][1])
                dp[i][k][0]=max(prices[i]+dp[i+1][k-1][1],dp[i+1][k][0])
        return dp[0][2][1]