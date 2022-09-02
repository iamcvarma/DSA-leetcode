class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q=deque([(0,'b'),(0,'r')])
        res,steps=[-1]*n,0
        seen=set()
        adj=defaultdict(list)
        for x,y in redEdges:
            adj[x].append((y,'r'))
        for x,y in blueEdges:
            adj[x].append((y,'b'))

        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                if curr in seen:continue
                seen.add(curr)
                if res[curr[0]]==-1 or res[curr[0]]>steps:
                    res[curr[0]]=steps
                for nei in adj[curr[0]]:
                    if nei[1]!=curr[1]:
                        q.append(nei)
            steps+=1
        return res
            