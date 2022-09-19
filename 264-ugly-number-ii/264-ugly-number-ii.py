class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i=j=k=0
        dp=[0]*n
        dp[0]=1
        for m in range(1,n):
            a,b,c = dp[i]*2,dp[j]*3,dp[k]*5
            dp[m] = min(a,b,c)
            if dp[m]==a:i+=1
            if dp[m]==b:j+=1
            if dp[m]==c:k+=1
        return dp[-1]