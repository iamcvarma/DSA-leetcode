class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:
        words=set(wordList)
        if start==end:return 0
        if end not in words:return 0
        seen=set([start])
        q=deque([start])
        dist=1
        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                for i in range(len(curr)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new=curr[:i]+c+curr[i+1:]
                        if new==end:return dist+1
                        if new in words and new not in seen:
                            q.append(new)
                            seen.add(new)
            dist+=1
        return 0
                            