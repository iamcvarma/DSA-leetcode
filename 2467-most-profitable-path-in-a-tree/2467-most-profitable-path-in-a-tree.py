class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        n = len(amount)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        parent = [-1 for _ in range(n+1)]
        time = [0 for _ in range(n+1)]
        
        def dfs(curr,par,t):
            parent[curr] = par
            time[curr] = t
            t+=1
            for nei in adj[curr]:
                if nei != par:
                    dfs(nei,curr,t)
            return
        dfs(0,None,0)
        
        t=0
        curr = bob
        while curr:
            if t<time[curr]:
                amount[curr]=0
            elif t==time[curr]:
                amount[curr]//=2
            curr = parent[curr]
            t+=1
        ma=-inf
        def main_dfs(curr,par,cost):
            nonlocal ma
            if curr and len(adj[curr])==1:
                ma=max(ma,cost+amount[curr])
                return
            for nei in adj[curr]:
                if nei != par:
                    main_dfs(nei,curr,cost+amount[curr])
            return
        main_dfs(0,None,0)
        return ma