class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank=set(bank)
        seen=set([start])
        q=deque([start])
        dist=0
        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                if curr==end:return dist
                for i in range(8):
                    for c in "ACGT":
                        new=curr[:i]+c+curr[i+1:]
                        if new in bank and new not in seen:
                            q.append(new)
                            seen.add(new)
            dist+=1
        return -1