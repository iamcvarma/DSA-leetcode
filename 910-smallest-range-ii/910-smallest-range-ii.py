class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi,ma = nums[0],nums[-1]
        res = ma-mi
        for i in range(len(nums)-1):
            lower = max(ma-k,nums[i]+k)
            upper = min(mi+k,nums[i+1]-k)
            res = min(res,abs(upper-lower))
        return res