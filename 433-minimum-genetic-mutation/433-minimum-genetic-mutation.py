class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:return -1
        q = deque([end])
        steps=1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for i in range(8):
                    for c in 'ACGT':
                        if c==curr[i]:continue
                        new = curr[:i]+c+curr[i+1:]
                        if new == start:return steps
                        if new in bank:
                            q.append(new)
                            bank.remove(new)
            steps+=1
        return -1