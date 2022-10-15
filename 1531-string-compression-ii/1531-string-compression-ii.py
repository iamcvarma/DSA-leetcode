class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def solve(i,char,run,deletes):
            if i==len(s):
                return 0
            key = (i,char,run,deletes)
            if key in dp:return dp[key]
            rem = inf
            if deletes>0:
                rem = solve(i+1,char,run,deletes-1)
            cost = 0
            if s[i]==char:
                t= 1 if run==1 or len(str(run+1))>len(str(run)) else 0
                cost = t + solve(i+1,char,run+1,deletes)
            else:
                cost = 1+solve(i+1,s[i],1,deletes)
            dp[key] = min(rem,cost)
            return dp[key]
        dp ={}
        return solve(0,"",0,k)