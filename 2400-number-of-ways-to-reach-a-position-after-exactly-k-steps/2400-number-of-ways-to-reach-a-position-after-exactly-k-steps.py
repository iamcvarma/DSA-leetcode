class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:
        def solve(i,k):
            if i==e and k==0:return 1
            if k<0:return 0
            key=(i,k)
            if key in dp:return dp[key]
            dp[key] = (solve(i-1,k-1)+solve(i+1,k-1))%mod
            return dp[key]
        dp={}
        mod=1000000007
        return solve(s,k)
                