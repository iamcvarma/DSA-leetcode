class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.end = False
    
    def add(self,word):
        curr = self
        for w in word:
            curr = curr.children[w]
        curr.end=word
        return
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n,res = len(board),len(board[0]),[]
        hmap=defaultdict(int)
        for i in range(m):
            for j in range(n):
                hmap[board[i][j]]+=1
        Tree = Trie()
        for word in words: 
            cc = Counter(word)
            for c in cc:
                if cc[c]>hmap[c]:break
            else:Tree.add(word)
        
        def dfs(i,j,curr,res):
            c = board[i][j]
            if c not in curr.children:return
            curr = curr.children[c]
            if curr.end:
                res.append(curr.end)
                curr.end=False
            board[i][j] = '*'
            if i>0:dfs(i-1,j,curr,res)
            if j>0:dfs(i,j-1,curr,res)
            if i<m-1: dfs(i+1,j,curr,res)
            if j<n-1:dfs(i,j+1,curr,res)
            
            board[i][j] = c
            return
        
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,Tree,res)
        return res