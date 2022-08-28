class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:return -1
        n=len(grid)
        q=deque([(0,0,1)])
        grid[0][0]=1
        while q:
            i,j,d=q.popleft()
            if i==n-1 and j==n-1:return d
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)):
                if x<0 or y<0 or x>=n or y>=n or grid[x][y]:continue
                grid[x][y]=1
                q.append((x,y,d+1))
        return -1