class Solution:
    def minNumberOfHours(self, e: int, x: int, en: List[int], ex: List[int]) -> int:
        res=0
        for i in range(len(en)):
            if en[i]>=e:
                res+=en[i]-e+1
                e=1
            else:e-=en[i]
            if ex[i]>=x:
                res+=ex[i]-x+1
                x=2*ex[i]+1
            else:x+=ex[i]
        return res