class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bsearch(target):
            s,e = 0,len(nums)-1
            while s<e:
                m = s+e>>1
                if dp[m]>=target:
                    e=m
                else:
                    s=m+1
            return e
        dp = [inf]*len(nums)
        ma = 0
        for n in nums:
            i = bisect.bisect_left(dp,n)
            dp[i] = min(dp[i],n)
            ma = max(ma,i)
        return ma+1