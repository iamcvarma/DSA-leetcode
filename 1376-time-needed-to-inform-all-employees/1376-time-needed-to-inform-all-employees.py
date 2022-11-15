class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(curr):
            ans=0
            for emp in adj[curr]:
                ans=max(ans,dfs(emp))
            return informTime[curr]+ans
        
        
        adj=defaultdict(list)
        for i,v in enumerate(manager):
            adj[v].append(i)
        return dfs(headID)
        