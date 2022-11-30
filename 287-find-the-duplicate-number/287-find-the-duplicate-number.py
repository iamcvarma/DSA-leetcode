class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #bsearch
        def check(m):
            return sum(i<=m for i in nums)<=m
        s,e = 1,len(nums)-1
        while s<e:
            m = s+e>>1
            if check(m):
                s=m+1
            else:
                e=m
        return s