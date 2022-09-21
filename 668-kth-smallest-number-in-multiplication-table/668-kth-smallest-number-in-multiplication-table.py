class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(mid):
            count = 0
            for i in range(1,n+1):
                count+=min(m*i,mid)//i
            return count>=k
        s,e = 1,m*n
        while s<e:
            mid = s+e>>1
            if check(mid):
                e = mid
            else :
                s = mid+1
        return e