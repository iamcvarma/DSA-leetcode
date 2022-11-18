class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def solve(i):
            if i>=n: return 0
            if i in dp: return dp[i]
            dp[i]=max(jobs[i][2]+solve(bisect.bisect_left(jobs,jobs[i][1],key = lambda x:x[0])),solve(i+1)) 
            return dp[i]
        
        n = len(profit)
        jobs=[]
        dp={}
        for i in range(n):
            jobs.append((startTime[i],endTime[i],profit[i]))
        jobs.sort(key = lambda x:x[0])
        
        return solve(0)
        