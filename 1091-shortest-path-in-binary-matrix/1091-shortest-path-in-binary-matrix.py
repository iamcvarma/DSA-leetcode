#A* path finding algorigthm

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:return -1
        n=len(grid)
        target=(n-1,n-1)
        score={(0,0):2*n}
        heap=[(2*n,1,0,0)]
        while heap:
            f,g,i,j=heapq.heappop(heap)
            if (i,j)==target:return g
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)):
                if x<0 or y<0 or x>=n or y>=n or grid[x][y]:continue
                heu=max(abs(x-n),abs(y-n))
                f=heu+g+1
                key=(x,y)
                if key not in score or score[key]>f:
                    score[key]=f
                    heapq.heappush(heap,(f,g+1,x,y))
        return -1