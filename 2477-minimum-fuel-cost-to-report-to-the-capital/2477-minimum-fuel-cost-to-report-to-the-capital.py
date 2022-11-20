class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def dfs(root,pre):
            nonlocal ans
            total = 1
            for ch in adj[root]:
                if ch!=pre:
                    total+=dfs(ch,root)
            if root:
                ans+=math.ceil(total/seats)
            return total
        ans=0
        adj = defaultdict(list)
        for x,y in roads:
            adj[x].append(y)
            adj[y].append(x)
        dfs(0,-1)
        return ans
            