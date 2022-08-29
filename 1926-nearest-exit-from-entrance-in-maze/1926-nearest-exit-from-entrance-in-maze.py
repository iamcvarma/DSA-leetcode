class Solution:
    def nearestExit(self, grid: List[List[str]], ent: List[int]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque([])
        grid[ent[0]][ent[1]]='*'
        for i in range(m):
            if grid[i][0]=='.':
                q.append((i,0))
            if grid[i][n-1]=='.':
                q.append((i,n-1))
        for j in range(n):
            if grid[0][j]=='.':
                q.append((0,j))
            if grid[m-1][j]=='.':
                q.append((m-1,j))
        steps=0
        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
                if ent==[i,j]:return steps
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if -1<x<m and -1<y<n and grid[x][y]!='+':
                        q.append((x,y))
                        grid[x][y]='+'
            steps+=1
        return -1