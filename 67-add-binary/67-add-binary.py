class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n = len(a),len(b)
        res=[]
        carry=0
        for i in range(max(m,n)):
            x = int(a[m-i-1]) if i<m else 0
            y = int(b[n-i-1]) if i<n else 0
            ans = x+y+carry
            res.append(ans%2)
            carry = ans//2
        if carry:res.append(carry)
        return "".join([str(c) for c in res[::-1]])