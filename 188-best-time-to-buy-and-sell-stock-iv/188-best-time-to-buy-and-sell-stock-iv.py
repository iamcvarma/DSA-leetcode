class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0,0] for _ in range(k+1)] for __ in range(n+1)]
        for i in range(n-1,-1,-1):
            for cap in range(1,k+1):
                dp[i][cap][1]=max(-prices[i]+dp[i+1][cap][0],dp[i+1][cap][1])
                dp[i][cap][0]=max(prices[i]+dp[i+1][cap-1][1],dp[i+1][cap][0])
        return dp[0][k][1]