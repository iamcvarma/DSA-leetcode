class Solution:
    def minDays(self, bloomDay: List[int], bq: int, k: int) -> int:
        def check(m):
            curr=t=0
            for n in bloomDay:
                if n<=m:
                    t+=1
                    curr+=t//k
                    t = t%k
                else:
                    t=0
            return curr>=bq
        
        if len(bloomDay)<bq*k:return -1
        s,e =1,max(bloomDay)
        while s<e:
            m = s+e>>1
            if check(m):
                e=m
            else:
                s=m+1
        return e