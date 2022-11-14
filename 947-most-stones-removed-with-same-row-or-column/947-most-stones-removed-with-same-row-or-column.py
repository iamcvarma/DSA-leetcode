class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank = [1]*n
        self.comp = n
    
    def find(self,curr):
        if curr==self.parent[curr]:
            return curr
        self.parent[curr] = self.find(self.parent[curr])
        return self.parent[curr]
    
    def union(self,a,b):
        a=self.find(a)
        b = self.find(b)
        if a==b: return
        if self.rank[a]>self.rank[b]:
            self.parent[b]=a
            self.rank[a]+=b
        else:
            self.parent[a] = b
            self.rank[b]+=a
        self.comp-=1
        return
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        ds = DSU(n)
        row={}
        col={}
        for i,arr in enumerate(stones):
            x,y = arr
            if x in row:
                ds.union(row[x],i)
            else:
                row[x]=i
            if y in col:
                ds.union(col[y],i)
            else:
                col[y]=i
        return n-ds.comp
                