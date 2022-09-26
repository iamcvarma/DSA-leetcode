class DSU:
    def __init__(self,n):
        self.comp = n
        self.parent = [i for i in range(n)]
        self.rank= [1]*n
    
    def find(self,c):
        if c==self.parent[c]:
            return c
        self.parent[c]=self.find(self.parent[c])
        return self.parent[c]
    
    def union(self,a,b):
        a=self.find(a)
        b = self.find(b)
        if a==b:return
        if self.rank[a]<self.rank[b]:
            a,b = b,a
        self.parent[b]=a
        self.rank[a]+=self.rank[b]
        self.comp-=1
        return
        
class Solution:
    def equationsPossible(self, arr: List[str]) -> bool:
        dd = DSU(26)
        a = ord('a')
        for s in arr:
            if s[1]=='=':
                dd.union(ord(s[0])-a,ord(s[-1])-a)
        for s in arr:
            if s[1]=='!':
                if s[0]==s[-1] or dd.find(ord(s[0])-a)==dd.find(ord(s[-1])-a):
                    return False
        return True
            