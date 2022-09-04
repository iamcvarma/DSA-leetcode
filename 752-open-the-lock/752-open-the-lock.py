class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        q=deque(["0000"])
        if "0000" in deadends:return -1
        deadends.add("0000")
        dist=0
        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                if curr==target:return dist
                for i in range(4):
                    new=curr[:i]+str((10+int(curr[i])+1)%10)+curr[i+1:]
                    if new not in deadends:
                        q.append(new)
                        deadends.add(new)
                    new=curr[:i]+str((10+int(curr[i])-1)%10)+curr[i+1:]
                    if new not in deadends:
                        q.append(new)
                        deadends.add(new)
            dist+=1
        return -1