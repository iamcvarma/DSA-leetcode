class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDeg,outDeg = [0]*n,[0]*n
        for x, y in trust:
            inDeg[y-1]+=1
            outDeg[x-1]+=1
        for i in range(n):
            if outDeg[i]==0 and inDeg[i]==n-1:
                return i+1
        return -1