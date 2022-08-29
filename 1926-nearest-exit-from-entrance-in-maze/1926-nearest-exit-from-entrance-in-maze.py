class Solution:
    def nearestExit(self, grid: List[List[str]], ent: List[int]) -> int:
        m,n=len(grid),len(grid[0])
        q=[(ent[0],ent[1])]
        grid[ent[0]][ent[1]]='+'
        steps=0
        while q:
            new=[]
            for i,j in q:
                if (i==0 or i==m-1 or j==0 or j==n-1) and [i,j]!=ent:return steps
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if -1<x<m and -1<y<n and grid[x][y]!='+':
                        new.append((x,y))
                        grid[x][y]='+'
            steps+=1
            q=new
        return -1