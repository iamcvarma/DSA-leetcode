class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        q = deque([(0,0,k)])
        seen = set()
        steps=0
        while q:
            for _ in range(len(q)):
                i,j,k = q.popleft()
                if k<0:continue
                if i==m-1 and j==n-1:
                    return steps
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if -1<x<m and -1<y<n and (x,y,k-grid[x][y]) not in seen:
                        q.append((x,y,k-grid[x][y]))
                        seen.add((x,y,k-grid[x][y]))
            steps+=1
        return -1