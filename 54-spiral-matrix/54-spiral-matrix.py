class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m,n = len(matrix),len(matrix[0])
        x,y = 0,1
        i,j=0,0
        while len(res)<m*n:
            res.append(matrix[i][j])
            matrix[i][j] = '*'
            i,j=i+x,j+y
            if i<0 or i>=m or j<0 or j>=n or matrix[i][j]=='*':
                i,j = i-x,j-y
                x,y = y,-x
                i,j=i+x,j+y
        return res