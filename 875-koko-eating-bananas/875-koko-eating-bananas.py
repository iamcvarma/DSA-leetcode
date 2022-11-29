class Solution:
    def minEatingSpeed(self, arr: List[int], h: int) -> int:
        def check(k):
            return sum(ceil(n/k) for n in arr)<=h
        s,e = 1,max(arr)
        while s<e:
            m = s+e>>1
            if check(m):
                e=m
            else:
                s=m+1
        return e