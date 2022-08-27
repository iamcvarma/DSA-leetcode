class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        def dfs(i,j,seen):
            if i<0 or j<0 or i>=m or j>=n or (i,j) in seen:return
            seen.add((i,j))
            curr=grid[i][j]
            if i>0 and grid[i-1][j]>=curr:dfs(i-1,j,seen)
            if j>0 and grid[i][j-1]>=curr:dfs(i,j-1,seen)
            if i<m-1 and grid[i+1][j]>=curr:dfs(i+1,j,seen)
            if j<n-1 and grid[i][j+1]>=curr:dfs(i,j+1,seen)
            return 
        pas=set()
        atl=set()
        for i in range(m):
            dfs(i,0,pas)
            dfs(i,n-1,atl)
        for j in range(n):
            dfs(0,j,pas)
            dfs(m-1,j,atl)
        return [[x,y] for x,y in pas&atl]