class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[0]*(3) for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                for k in range(1,3):
                    if buy:
                        dp[i][buy][k]=max(-prices[i]+dp[i+1][0][k],dp[i+1][1][k])
                    else:
                        dp[i][buy][k]=max(prices[i]+dp[i+1][1][k-1],dp[i+1][0][k])
        return dp[0][1][2]