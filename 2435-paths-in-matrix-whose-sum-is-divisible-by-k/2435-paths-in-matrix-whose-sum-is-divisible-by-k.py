class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod=1000000007
        m,n=len(grid)+1,len(grid[0])+1
        dp=[[[0]*(k) for __ in range(n)] for _ in range(m)]
        dp[1][1][grid[0][0]%k]=1
        for i in range(1,m):
            for j in range(1,n):
                for pre in range(k):
                    dp[i][j][(grid[i-1][j-1]+pre)%k]+=(dp[i-1][j][pre]+dp[i][j-1][pre])%mod
        return dp[m-1][n-1][0]
    