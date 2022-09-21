class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def check(m):
            i,j=0,0
            count=0
            while i<n:
                while j<n and nums[j]-nums[i]<=m:
                    j+=1
                count+=j-i-1
                i+=1
            return count>=k
        nums.sort()
        n = len(nums)
        s,e = 0, max(nums)-min(nums)
        while s<e:
            m = s+e>>1
            if check(m):
                e= m
            else:
                s = m+1
        return s