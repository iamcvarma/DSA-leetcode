class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s=sorted(str(n))
        x=1<<32
        while x:
            new=sorted(str(x))
            if s==new:return True
            if len(new)<len(s):break
            x=x>>1
            
        return False
        