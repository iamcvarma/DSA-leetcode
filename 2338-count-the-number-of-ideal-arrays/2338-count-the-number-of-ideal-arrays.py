class Solution:
    def idealArrays(self, n: int, ma: int) -> int:
        def solve(pre,i):
            if i==n:return 1
            k = (pre,i)
            if k not in dp:
                dp[k] = (sum((solve(j,i+1) for j in range(pre*2,ma+1,pre)))+comb(n,i))%mod
            return dp[k]
        dp={}
        mod = 10**9+7
        return solve(1,0)
                