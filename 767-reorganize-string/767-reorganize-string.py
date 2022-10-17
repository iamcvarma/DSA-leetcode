class Solution:
    def reorganizeString(self, s: str) -> str:
        n  = len(s)
        res = [0]*n
        i=0
        cc= list(Counter(s).items())
        cc.sort(key = lambda x:(-x[1]))
        if cc[0][1]>((n-1)//2)+1:return ""
        for ch,num in cc:
            while num:
                res[i]=ch
                num-=1
                i+=2
                if i>=n:i=1
        return "".join(res)