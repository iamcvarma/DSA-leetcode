class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=0
        carry = 0
        for j,n in enumerate(num1):
            carry = 0
            temp = 0
            for i,m in enumerate(num2[::-1]):
                ans = int(n)*int(m)+carry
                temp+=(ans%10)*10**i
                carry = ans//10
            if carry:temp+=carry*(10**(i+1))
            res+=temp*(10**(len(num1)-j-1))
        return str(res)