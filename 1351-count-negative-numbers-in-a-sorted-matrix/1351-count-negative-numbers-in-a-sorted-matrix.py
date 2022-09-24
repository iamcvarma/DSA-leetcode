class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        i,res=0,0
        for j in range(n-1,-1,-1):
            while i<m and grid[i][j]>=0:
                i+=1
            res+=m-i
        return res