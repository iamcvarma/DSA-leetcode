class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        flag=True
        def dfs(curr,c):
            nonlocal flag
            if not flag:return
            if color[curr]==1-c:
                flag=False
                return
            if color[curr]==c:return
            color[curr]=c
            for nei in graph[curr]:
                dfs(nei,1-c)
        
        for i in range(n):
            if color[i]==-1:
                dfs(i,0)
            if not flag:return False
        return True