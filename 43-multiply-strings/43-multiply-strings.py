class Solution:
    def multiply(self, a: str, b: str) -> str:
        res=[0]*(len(a)+len(b))
        a=a[::-1]
        b=b[::-1]
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                res[i+j]+=int(x)*int(y)
        for i in range(len(res)-1):
            res[i+1]+=res[i]//10
            res[i]%=10
        res = "".join(map(str,res))[::-1]
        return str(int(res))