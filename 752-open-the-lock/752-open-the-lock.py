class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        start="0000"
        if target==start:return 0
        if start in deadends:return -1
        q1,q2=set([start]),set([target])
        deadends.add(start)
        deadends.add(target)
        dist=0
        while q1:
            if len(q1)>len(q2):
                q1,q2=q2,q1
            new=set()
            for curr in q1:
                for i in range(4):
                    num=int(curr[i])
                    for c in ((num+1)%10,(10+num-1)%10):
                        code=curr[:i]+str(c)+curr[i+1:]
                        if code in q2:return dist+1
                        if code not in deadends:
                            deadends.add(code)
                            new.add(code)
            q1=new
            dist+=1
        return -1