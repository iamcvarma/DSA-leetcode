class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0]*n for _ in range(n)]
        x,y=0,1
        i,j=0,0
        for num in range(n*n):
            arr[i][j]=num+1
            if not (-1<i+x<n) or not (-1<j+y<n) or arr[i+x][j+y]:
                x,y = y,-x
            i+=x
            j+=y
        return arr