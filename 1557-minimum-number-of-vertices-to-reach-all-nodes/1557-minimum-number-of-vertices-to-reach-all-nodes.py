class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        deg = [0]*n
        for x,y in edges:
            deg[y]+=1
        return [i for i in range(n) if not deg[i]]