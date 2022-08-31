class DSU:
    def __init__(self,size):
        self.parent=list(range(size))
        self.rank=[1]*size
        self.comp=size
        return
    def find(self,curr):
        if self.parent[curr]==curr:
            return curr
        self.parent[curr]=self.find(self.parent[curr])
        return self.parent[curr]
    
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a==b:return
        self.comp-=1
        if self.rank[a]>self.rank[b]:
            self.parent[b]=a
            self.rank[a]+=self.rank[b]
        else:
            self.parent[a]=b
            self.rank[b]+=self.rank[a]
        return
    
class Solution:
    def findCircleNum(self, adj: List[List[int]]) -> int:
        n=len(adj)
        dset=DSU(n)
        for i in range(n):
            for j in range(n):
                if adj[i][j]:
                    dset.union(i,j)
        return dset.comp