class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while i*i<num:i*=2
        s,e = i//2,i
        while s<=e:
            m=s+e>>1
            sq = m*m
            if sq<num:
                s=m+1
            elif sq>num:
                e=m-1
            else:return True
        return False