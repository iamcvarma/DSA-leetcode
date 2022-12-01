class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(m):
            count = 0
            for n in dist[:-1]:
                count+=ceil(n/m)
            count+=dist[-1]/m
            return count<=hour
        
        s,e = 1,100000000
        if not check(100000000):return -1
        while s<e:
            m = s+e>>1
            if check(m):
                e=m
            else:s=m+1
        return s 