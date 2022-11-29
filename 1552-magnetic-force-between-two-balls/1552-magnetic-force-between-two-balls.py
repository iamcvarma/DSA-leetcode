class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        def check(d):
            pre,ans = pos[0],1
            for i in range(n):
                if pos[i]-pre>=d:
                    ans+=1
                    pre= pos[i]
            return ans
        pos.sort()
        n = len(pos)
        s,e = 1,pos[-1]-pos[0]
        while s<e:
            mid = s+e+1>>1
            if check(mid)>=m:
                s= mid
            else:
                e= mid-1
        return s