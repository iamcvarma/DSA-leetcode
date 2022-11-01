class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDeg,outDeg = [0]*(n+1),[0]*(n+1)
        for x, y in trust:
            inDeg[y]+=1
            outDeg[x]+=1
        for i in range(1,n+1):
            if outDeg[i]==0 and inDeg[i]==n-1:
                return i
        return -1