class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        q = deque([tuple(entrance)])
        a,b = entrance
        maze[a][b]='+'
        steps=0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if [i,j]!=entrance:
                        return steps
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if -1<x<m and -1<y<n and maze[x][y]=='.':
                        q.append((x,y))
                        maze[x][y]='+'
            steps+=1
        return -1
                