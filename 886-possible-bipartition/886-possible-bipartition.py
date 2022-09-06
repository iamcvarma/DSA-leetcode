class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(curr,g):
            if group[curr]==1-g:return False
            if group[curr]==g:return True
            group[curr]=g
            for nei in adj[curr]:
                if not dfs(nei,1-g):
                    return False
            return True
        adj=defaultdict(list)
        group=[-1]*(n+1)
        for x,y in dislikes:
            adj[x].append(y)
            adj[y].append(x)
        for i in range(1,n+1):
            if group[i]==-1 and not dfs(i,0):
                return False
        return True