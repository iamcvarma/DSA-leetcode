class Solution:
    def numSquares(self, n: int) -> int:
        sqrs = []
        i=sq=1
        while sq<=n:
            sqrs.append(sq)
            i+=1
            sq=i*i
        dp=[0]+[inf]*n
        for i in range(1,n+1):
            for j in sqrs:
                if j>i:break
                dp[i] = min(dp[i],dp[i-j]+1)
        return dp[-1]