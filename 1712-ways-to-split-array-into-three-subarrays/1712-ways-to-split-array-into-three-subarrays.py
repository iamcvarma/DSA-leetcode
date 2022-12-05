class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        res,n=0,len(nums)
        for i in range(1,n): nums[i]+=nums[i-1]
        for i in range(n):
            j = max(bisect.bisect_left(nums,2*nums[i]),i+1)
            k = min(bisect.bisect_right(nums,(nums[-1]+nums[i])//2),n-1)
            res+=max(0,k-j)
        return res%(10**9+7)