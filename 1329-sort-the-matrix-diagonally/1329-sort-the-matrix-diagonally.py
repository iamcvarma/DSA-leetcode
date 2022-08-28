class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def solve(i,j,heap):
            if i>=m or j>=n:return
            heapq.heappush(heap,-mat[i][j])
            solve(i+1,j+1,heap)
            mat[i][j]=-heapq.heappop(heap)
            return
        m,n=len(mat),len(mat[0])
        for i in range(m):
            solve(i,0,[])
        for j in range(1,n):
            solve(0,j,[])
        return mat