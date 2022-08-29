class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)
        q=set()
        def dfs(i,j):
            if grid[i][j]==0:
                q.add((i,j))
                grid[i][j]=-1
            else:
                grid[i][j]=-1
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if -1<x<n and -1<y<n and grid[x][y]!=-1:
                        dfs(x,y)
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    mx,my=i,j
                    break
        dfs(mx,my)
        dist=1
        while q:
            new=[]
            for i,j in q:
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if -1<x<n and -1<y<n:
                        if grid[x][y]==1:
                            return dist
                        elif grid[x][y]==0:
                            grid[x][y]=-1
                            new.append((x,y))
            q=new
            dist+=1
        return -1