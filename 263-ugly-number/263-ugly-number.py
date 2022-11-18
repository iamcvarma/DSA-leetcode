class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:return False
        for d in (5,3,2):
            while not n%d: n//=d
        return n==1