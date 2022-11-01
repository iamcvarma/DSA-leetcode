class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        @cache
        def dfs(i,j):
            if i==m:return j
            if grid[i][j]==1 and j+1<n and grid[i][j+1]==1:
                return dfs(i+1,j+1)
            elif grid[i][j]==-1 and -1<j-1 and grid[i][j-1]==-1:
                return dfs(i+1,j-1)
            else:return -1
        m,n = len(grid),len(grid[0])
        return [dfs(0,j) for j in range(n)]
                