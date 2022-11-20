class Solution:
    def beautifulPartitions(self, s: str, k: int, mi: int) -> int:
        primes=set("2357")
        if s[0] not in primes:return 0
        if s[-1] in primes:return 0
        mod = 1000000007
        n = len(s)
        @cache
        def solve(i,k):
            if k==1 and i<=n:return 1
            if i>=n:return 0
            ans = solve(i+1,k)
            if s[i] in primes and s[i-1] not in primes:
                ans=(ans+solve(i+mi,k-1))
            
            return ans%mod
        
        return solve(mi,k)