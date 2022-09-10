class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        dp=[{} for _ in range(n)]
        for i in range(n):
            dp[i][0]=1
            for j in range(i):
                diff = nums[i]-nums[j]
                if diff in dp[j]:
                    dp[i][diff]=dp[j][diff]+1
                else:dp[i][diff]=2
            res=max(res,max(dp[i].values()))
        return res