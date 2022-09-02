class Solution:
    res=0
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node,pre):
            if node in ori[pre]:
                self.res+=1
            for child in adj[node]:
                if child!=pre:
                    dfs(child,node)
            return
        
        
        adj=defaultdict(list)
        ori=defaultdict(list)
        
        for x, y in connections:
            ori[x].append(y)
            adj[x].append(y)
            adj[y].append(x)
        dfs(0,-1)
        return self.res