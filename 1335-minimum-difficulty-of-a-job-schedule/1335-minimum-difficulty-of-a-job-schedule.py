class Solution:
    def minDifficulty(self, job: List[int], d: int) -> int:
        if len(job)<d:return -1
        def solve(i,day,curr_ma):
            if not day:
                if i<len(job):return inf
                return curr_ma
            if i==len(job):return inf
            key = (i,day,curr_ma)
            if key in dp:return dp[key]
            dp[key] = min(solve(i+1,day,max(curr_ma,job[i])) , max(curr_ma,job[i]) + solve(i+1,day-1,0))
            return dp[key]
        dp={}
        return solve(0,d,0)