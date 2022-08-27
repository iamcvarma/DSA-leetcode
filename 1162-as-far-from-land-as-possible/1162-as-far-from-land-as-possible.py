class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        q=deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i+1,j))
                    q.append((i-1,j))
                    q.append((i,j+1))
                    q.append((i,j-1))
        steps=1
        while q:
            steps+=1
            for _ in range(len(q)):
                x,y=q.popleft()
                if x<0 or y<0 or x>=n or y>=n or grid[x][y]!=0:continue
                grid[x][y]=steps
                q.append((x+1,y))
                q.append((x-1,y))
                q.append((x,y+1))
                q.append((x,y-1))          
        return steps-2 if steps-2!=0 else -1
            
            