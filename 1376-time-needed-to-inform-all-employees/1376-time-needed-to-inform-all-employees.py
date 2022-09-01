class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node,curr):
            nonlocal ma
            if informTime[node]==0:
                ma=max(ma,curr)
                return
            curr+=informTime[node]
            for sub in adj[node]:
                dfs(sub,curr)
            return
        ma=0
        adj=defaultdict(list)
        for i,v in enumerate(manager):
            adj[v].append(i)
        dfs(headID,0)
        return ma