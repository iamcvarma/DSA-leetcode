class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n  = len(heights),len(heights[0])
        dp = [[inf]*n for _ in range(m)]
        dp[0][0] = 0
        heap = [(0,0,0)]
        while heap:
            eff,i,j = heapq.heappop(heap)
            if i==m-1 and j==n-1:return eff
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if -1<x<m and -1<y<n:
                    new = max(eff,abs(heights[i][j]-heights[x][y]))
                    if new<dp[x][y]:
                        dp[x][y] = new
                        heapq.heappush(heap,(new,x,y))
        