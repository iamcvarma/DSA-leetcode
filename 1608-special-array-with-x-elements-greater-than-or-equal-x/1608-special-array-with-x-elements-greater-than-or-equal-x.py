class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def count(x):
            res = 0
            for n in nums:
                if n>=x:res+=1
            return res
        s,e = 0,len(nums)
        while s<=e:
            m = s+e>>1
            c = count(m)
            if m>c:
                e= m-1
            elif m<c:
                s =m+1
            else:
                return m
        return -1