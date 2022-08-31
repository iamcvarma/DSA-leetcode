class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:return -1
        adj=defaultdict(list)
        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
            
        def dfs(node):
            if node in seen:return
            seen.add(node)
            for nei in adj[node]:
                dfs(nei)

        seen=set()
        count=0
        for i in range(n):
            if i in seen:continue
            count+=1
            dfs(i)
        return count-1
        