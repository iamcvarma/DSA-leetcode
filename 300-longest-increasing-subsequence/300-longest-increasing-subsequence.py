class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [inf]*len(nums)
        ma = 1
        for n in nums:
            i = bisect.bisect_left(dp,n)
            dp[i] = min(dp[i],n)
            ma = max(ma,i+1)
        return ma