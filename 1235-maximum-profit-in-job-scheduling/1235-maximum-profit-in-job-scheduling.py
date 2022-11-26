class Solution:
    def jobScheduling(self, start: List[int], end: List[int], profit: List[int]) -> int:
        def solve(i):
            if i>=n:return 0
            if i in dp:return dp[i]
            dp[i] = max(solve(i+1),arr[i][2]+solve(bisect.bisect_left(arr,arr[i][1],key = lambda x:x[0])))
            return dp[i]
        dp={}
        arr = sorted(zip(start,end,profit),key = lambda x:x[0])
        n = len(arr)
        return solve(0)