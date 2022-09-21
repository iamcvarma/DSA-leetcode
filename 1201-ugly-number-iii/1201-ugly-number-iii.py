class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = (a*b)//math.gcd(a,b)
        bc = (b*c)//math.gcd(b,c)
        ac = (a*c)//math.gcd(a,c)
        
        abc = (a*bc)//math.gcd(a,bc)
        
        def cond(m):
            k = m//a+m//b+m//c-m//ab-m//bc-m//ac+m//abc
            return k>=n
        
        s,e = 1,2*10**9
        while s<e:
            m = s+e>>1
            if cond(m):
                e=m
            else:s = m+1
        return e