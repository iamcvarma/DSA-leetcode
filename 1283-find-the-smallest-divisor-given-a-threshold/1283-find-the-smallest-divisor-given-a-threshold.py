class Solution:
    def smallestDivisor(self, nums: List[int], target: int) -> int:
        if sum(nums)<=target:return 1
        
        def cond(m):
            return sum((n-1)//m+1 for n in nums)<=target
        
        s,e = 1,max(nums)
        while s<e:
            m = s+e>>1
            if cond(m):
                e = m
            else:
                s = m+1
        return e
        