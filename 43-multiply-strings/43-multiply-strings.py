class Solution:
    def multiply(self, a: str, b: str) -> str:
        m,n = len(a),len(b)
        res=[0]*(m+n)
        
        for i in range(m):
            for j in range(n):
                ans = res[i+j]+int(a[m-i-1])*int(b[n-j-1])
                res[i+j] = ans%10
                res[i+j+1] +=ans//10
    
        res = "".join(map(str,res))[::-1]
        return str(int(res))