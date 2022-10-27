class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def process(s,a,b):
            res=[]
            count=0
            for c in s:
                if c==a:
                    count+=1
                    res.append(c)
                elif c==b:
                    if count>0:
                        count-=1
                        res.append(c)
                else:
                    res.append(c)
            return res
        s1 = process(s,'(',')')
        s2 = process(s1[::-1],')','(')
        return "".join(s2[::-1])