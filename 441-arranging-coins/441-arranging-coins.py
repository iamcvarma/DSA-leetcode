class Solution:
    def arrangeCoins(self, n: int) -> int:
        s,e = 1,n
        while s<e:
            m = s+e+1>>1
            if (m*(m+1))//2<=n:
                s = m
            else :
                e=m-1
        return s