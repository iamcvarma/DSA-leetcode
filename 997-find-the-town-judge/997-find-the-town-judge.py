class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1:return 1
        deg=defaultdict(int)
        for x,y in trust:
            deg[x]-=1
            deg[y]+=1
        for g in deg:
            if deg[g]==n-1:
                return g
        return -1