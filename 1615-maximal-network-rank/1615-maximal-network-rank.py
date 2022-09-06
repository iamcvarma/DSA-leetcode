class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        matrix=[[0]*n for _ in range(n)]
        deg=defaultdict(int)
        ma=0
        for x,y in roads:
            matrix[x][y]=matrix[y][x]=1
            deg[x]+=1
            deg[y]+=1
        for i in range(n):
            for j in range(i+1,n):
                ma=max(ma,deg[i]+deg[j]-matrix[i][j])
        return ma