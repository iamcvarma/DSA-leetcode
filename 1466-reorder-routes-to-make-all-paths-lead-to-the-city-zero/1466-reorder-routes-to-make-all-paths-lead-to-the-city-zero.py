class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node,pre):
            res[0]+= 1 if (pre,node) in edges else 0
            for child in adj[node]:
                if child!=pre:dfs(child,node)
        
        res=[0]
        adj=defaultdict(list)
        edges={(x,y) for x,y in connections}
        for x, y in connections:
            adj[x].append(y)
            adj[y].append(x)
        dfs(0,-1)
        return res[0]