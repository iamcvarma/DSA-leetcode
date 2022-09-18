class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)
        while s<e:
            m = s+e>>1
            if nums[m]>=target:
                e=m
            else:
                s=m+1
        return e