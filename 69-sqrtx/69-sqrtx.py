class Solution:
    def mySqrt(self, x: int) -> int:
        s,e = 0,x//2+1
        while s<e:
            m = s+e+1>>1
            if m*m<=x: s = m
            else: e=m-1
        return s