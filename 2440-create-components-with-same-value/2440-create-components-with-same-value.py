class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        if len(nums)==1:return 0
        
        def topo(target):
            arr=nums[:]
            adj=defaultdict(set)
            for x,y in edges:
                adj[x].add(y)
                adj[y].add(x)
            q=deque([i for i in adj if len(adj[i])==1])
            while q:
                curr = q.popleft()
                if arr[curr]>target:return False
                else:
                    parent = list(adj[curr])[0]
                    adj[parent].remove(curr)
                    if arr[curr]<target:arr[parent]+=arr[curr]
                    if len(adj[parent])==1:
                        q.append(parent)
                    elif len(adj[parent])==0:
                        if arr[parent]==target:return True
                        else:return False
            return False
        s=sum(nums)
        for i in range(max(nums),s):
            if s%i==0 and topo(i):
                return s//i-1
        return 0