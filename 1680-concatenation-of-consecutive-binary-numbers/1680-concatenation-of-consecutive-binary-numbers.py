class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res=0
        mod = 1000000007
        for i in range(1,n+1):
            res = res<<int(math.log(i,2)+1)
            res = res%mod+i
        return res%mod
        