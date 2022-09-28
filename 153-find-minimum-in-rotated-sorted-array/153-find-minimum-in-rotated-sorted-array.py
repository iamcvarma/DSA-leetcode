class Solution:
    def findMin(self, nums: List[int]) -> int:
        s,e=0,len(nums)-1
        while s<e:
            m = s+e>>1
            if nums[m]<=nums[e]:
                e=m
            else:
                s=m+1
        return nums[e]