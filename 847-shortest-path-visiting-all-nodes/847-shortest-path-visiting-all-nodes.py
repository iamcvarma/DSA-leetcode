class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        if n==1:return 0
        q=deque([])
        end=(1<<n)-1
        seen=defaultdict(set)
        for i in range(n):
            q.append((i,1<<i))
            seen[i].add(1<<i)
        steps=0
        while q:
            for _ in range(len(q)):
                curr,visited=q.popleft()
                for nei in graph[curr]:
                    new=visited|1<<nei
                    if new==end:return steps+1
                    if new not in seen[nei]:
                        seen[nei].add(new)
                        q.append((nei,new))
            steps+=1
        return 