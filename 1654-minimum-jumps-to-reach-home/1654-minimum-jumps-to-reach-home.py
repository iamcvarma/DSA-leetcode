class Solution:
    def minimumJumps(self, forbid: List[int], a: int, b: int, x: int) -> int:
        seen=set(forbid)
        q=deque([(0,True)])
        limit=2000+a+b
        c=a-b
        dist=0
        while q:
            for _ in range(len(q)):
                i,flag=q.popleft()
                if i==x:return dist
                if not (-1<i<limit) or i in seen:continue
                seen.add(i)
                if flag:q.append((i-b,False))
                q.append((i+a,True))
            dist+=1
        return -1
                