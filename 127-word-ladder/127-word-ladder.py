class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:
        words=set(wordList)
        if start==end:return 0
        if end not in words:return 0
        q1,q2=set([start]),set([end])
        seen=set([start,end])
        dist=1
        while q1:
            if len(q1)>len(q2):
                q1,q2=q2,q1
            new=set()
            for curr in q1:
                for i in range(len(curr)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        word=curr[:i]+c+curr[i+1:]
                        if word in q2:return dist+1
                        if word in words and word not in seen:
                            new.add(word)
                            seen.add(word)
            dist+=1
            q1=new
        return 0
                            