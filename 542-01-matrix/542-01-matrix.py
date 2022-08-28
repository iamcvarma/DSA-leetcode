class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        q=deque([])
        seen=set()
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    q.append((i,j))
                    seen.add((i,j))
        while q:
            i,j=q.popleft()
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if -1<x<m and -1<y<n and (x,y) not in seen:
                    mat[x][y]=1+mat[i][j]
                    seen.add((x,y))
                    q.append((x,y))
        return mat
        
        