class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hmap={}
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if j-i in hmap and hmap[j-i]!=matrix[i][j]:
                    return False
                else: hmap[j-i] = matrix[i][j]
        return True