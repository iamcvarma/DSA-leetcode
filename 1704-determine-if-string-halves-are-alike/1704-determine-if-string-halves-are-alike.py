class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a,b=0,0
        n = len(s)//2
        for i,c in enumerate(s):
            if c in "aeiouAEIOU":
                if i<n:
                    a+=1
                else:
                    b+=1
        return a==b
                    