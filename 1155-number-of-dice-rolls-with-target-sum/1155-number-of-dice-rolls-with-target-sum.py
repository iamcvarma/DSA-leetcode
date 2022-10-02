class Solution:
    def numRollsToTarget(self, n: int, face: int, target: int) -> int:
        dp=[[0]*(target+1) for _ in range(n+1)]
        dp[0][0]=1
        mod=1000000007
        for i in range(1,n+1):
            for j in range(1,target+1):
                for k in range(1,face+1):
                    if k>j:break
                    dp[i][j]+=dp[i-1][j-k]
                dp[i][j]=(dp[i][j])%mod
        return dp[n][target]%mod