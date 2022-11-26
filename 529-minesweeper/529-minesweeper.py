class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def calc(i,j):
            count = 0
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)):
                if -1<x<m and -1<y<n and board[x][y]=='M':
                    count+=1
            return count
        
        def solve(i,j):
            nonlocal end
            if end or i<0 or j<0 or i>=m or j>=n or board[i][j] not in ('E','M'):
                return 
            if board[i][j]=='M':
                board[i][j]='X'
                end = True
                return
            count = calc(i,j)
            if count:
                board[i][j]=str(count)
            else:
                board[i][j] = 'B'
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)):
                    solve(x,y)
            return
        end = False
        m,n = len(board),len(board[0])
        solve(*click)
        
        return board
            