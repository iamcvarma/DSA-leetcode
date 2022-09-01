class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #topo
        n=len(graph)
        adj=defaultdict(list)
        degree=[0]*n
        q=deque([])
        for i,v in enumerate(graph):
            degree[i]=len(v)
            if degree[i]==0:q.append(i)
            for nodes in v:
                adj[nodes].append(i)
        while q:
            curr=q.popleft()
            for nei in adj[curr]:
                degree[nei]-=1
                if degree[nei]==0:
                    q.append(nei)
        return [i for i in range(n) if degree[i]==0]