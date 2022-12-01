class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        V = "aeiouAEIOU"
        n = len(s)//2
        vFilter = lambda x: x in V
        a = len(list(filter(vFilter,s[:n])))
        b = len(list(filter(vFilter,s[n:])))
        return a==b