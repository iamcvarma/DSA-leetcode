class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree=defaultdict(int)
        for x,y in edges:
            indegree[y]+=1
        return [i for i in range(n) if indegree[i]==0]