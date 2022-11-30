class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(m):
            return sum(ceil(n/m) for n in nums)<=threshold
        
        s,e = 1,max(nums)
        while s<e:
            m = s+e>>1
            if check(m):
                e=m
            else:
                s=m+1
        return e