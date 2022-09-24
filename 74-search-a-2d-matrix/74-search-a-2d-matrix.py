class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k,n = len(matrix),len(matrix[0])
        s,e = 0,k*n-1
        while s<=e:
            m = s+e>>1
            mid = matrix[m//n][m%n]
            if mid>target:
                e=m-1
            elif mid<target:
                s=m+1
            else:
                return True
        return False