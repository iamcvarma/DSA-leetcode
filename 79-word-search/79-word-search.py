class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            if k==len(word):
                return True
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if -1<x<m and -1<y<n and word[k]==board[x][y]:
                    board[x][y]='*'
                    if dfs(x,y,k+1):
                        return True
                    board[x][y]=word[k]
            return False
        m,n = len(board),len(board[0])
        B = defaultdict(int)
        W = Counter(word)
        for i in range(m):
            for j in range(n):
                B[board[i][j]]+=1
        for c in W:
            if W[c]>B[c]:
                return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    board[i][j]='*'
                    if dfs(i,j,1):
                        return True
                    board[i][j]=word[0]
        return False
        