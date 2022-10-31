class Solution:
    def maximumGood(self, A: List[List[int]]) -> int:
        def valid(arr,pattern):
            return all(x==int(y) for x,y in zip(arr,pattern) if x!=2)
        def check(pattern):
            return all(valid(A[i],pattern) for i,v in enumerate(pattern) if v=='1')
        res=0
        n = len(A)
        for i in range(1<<n,1<<(n+1)):
            pattern = bin(i)[3:]
            if check(pattern):
                res=max(res,pattern.count('1'))
        return res