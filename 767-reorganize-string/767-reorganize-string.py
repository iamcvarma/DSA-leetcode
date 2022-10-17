class Solution:
    def reorganizeString(self, s: str) -> str:
        n  = len(s)
        res = [0]*n
        i=0
        cc= Counter(s)
        s = sorted(s,key = lambda x: (-cc[x],x))
        print(s)
        for j in range(0,n,2):
            res[j] = s[i]
            i+=1
        for j in range(1,n,2):
            res[j] = s[i]
            i+=1
        print(res)
        for i in range(1,n):
            if res[i]==res[i-1]:
                return ""
        return "".join(res)