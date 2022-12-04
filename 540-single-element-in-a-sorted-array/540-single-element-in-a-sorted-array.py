class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s,e = 0,len(nums)-1
        while s<e:
            m = s+e>>1
            if (m&1 and nums[m-1]==nums[m]):
                s=m+1
            elif not m&1 and nums[m]==nums[m+1]:
                s=m+2
            else:
                e=m
        return nums[e]
                
                
                