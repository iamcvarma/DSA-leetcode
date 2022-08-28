class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_order(arr):
            q=deque([])
            adj=defaultdict(set)
            seen=set()
            rank=[0]*k
            res=[]
            for i,j in arr:
                if j-1 in adj[i-1]:continue
                adj[i-1].add(j-1)
                rank[j-1]+=1
            for i in range(k):
                if rank[i]==0:
                    q.append(i)
            
            while q:
                curr=q.popleft()
                if curr in seen:continue
                res.append(curr)
                seen.add(curr)
                for nei in adj[curr]:
                    rank[nei]-=1
                    if rank[nei]==0:q.append(nei)
            return res if len(res)==k else None
        
        res1,res2=topo_order(rowConditions),topo_order(colConditions)
        if not res1 or not res2:return []
        ans=[[0]*k for _ in range(k)]
        for i in range(k):
            ans[res1.index(i)][res2.index(i)]=i+1
        return ans
                    