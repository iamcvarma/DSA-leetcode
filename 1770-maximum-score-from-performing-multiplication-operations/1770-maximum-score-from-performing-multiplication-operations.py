class Solution:
    def maximumScore(self, nums: List[int], arr: List[int]) -> int:
        m,n = len(arr),len(nums)
        gap = n-m
        dp = [[0]*(m) for __ in range(m+1)]          
        for i in range(m-1,-1,-1):
            for j in range(i,m):
                k = m-(j-i+1)
                dp[i][j] = max(nums[i]*arr[k]+dp[i+1][j],nums[j+gap]*arr[k]+dp[i][j-1])
        return dp[0][m-1]