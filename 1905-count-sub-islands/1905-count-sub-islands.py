class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n=len(grid1),len(grid1[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid2[i][j]==0:return True
            if grid1[i][j]==0:return False
            grid2[i][j]=0
            a=dfs(i+1,j)
            b=dfs(i-1,j)
            c=dfs(i,j+1)
            d=dfs(i,j-1)
            return a and b and c and d
            
        res=0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1:
                    if dfs(i,j):
                        res+=1
        return res