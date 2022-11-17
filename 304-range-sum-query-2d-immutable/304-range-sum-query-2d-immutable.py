class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix),len(matrix[0])
        self.mat = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans = matrix[i][j]
                if i: ans+=self.mat[i-1][j]
                if j: ans+=self.mat[i][j-1]
                if i and j: ans-=self.mat[i-1][j-1]
                self.mat[i][j] = ans
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.mat[row2][col2]
        if row1: ans-=self.mat[row1-1][col2]
        if col1: ans-=self.mat[row2][col1-1]
        if row1 and col1: ans+=self.mat[row1-1][col1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)