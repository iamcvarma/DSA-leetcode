class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def check(M,T):
            for i in range(n):
                for j in range(n):
                    if M[i][j]!=T[i][j]:
                        return False
            return True
        
        def rotate(matrix):
            for i in range(n):
                for j in range(i+1,n):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
            for i in range(n):
                matrix[i] = matrix[i][::-1]
        n = len(mat)
        for _ in range(4):
            if check(mat,target):
                return True
            rotate(mat)
        return False