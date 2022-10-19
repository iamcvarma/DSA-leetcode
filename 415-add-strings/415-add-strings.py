class Solution:
    def addStrings(self, a: str, b: str) -> str:
        carry = 0
        res=[]
        i,j=len(a)-1,len(b)-1
        while i>-1 or j>-1:
            ans = (int(a[i]) if i>-1 else 0) + (int(b[j]) if j>-1 else 0) + (carry)
            res.append(str(ans%10))
            carry = ans//10
            i-=1
            j-=1
        if carry:res.append(str(carry))
        return "".join(reversed(res))