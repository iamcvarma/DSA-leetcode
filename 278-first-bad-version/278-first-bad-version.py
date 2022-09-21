# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s,e = 1,n
        while s<e:
            m = s+e>>1
            if isBadVersion(m):
                e = m
            else :
                s = m+1
        return e