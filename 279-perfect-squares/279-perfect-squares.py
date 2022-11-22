class Solution:
    def numSquares(self, n: int) -> int:
        q=deque([n])
        steps=0
        seen = set()
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                j = sq = 1
                while sq<=curr:
                    new = curr-sq
                    if (new) not in seen:
                        if new==0:return steps+1
                        seen.add(new)
                        q.append(new)
                    j+=1
                    sq=j*j
            steps+=1
        return -1