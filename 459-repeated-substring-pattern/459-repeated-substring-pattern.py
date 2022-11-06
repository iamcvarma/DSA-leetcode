class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i,c in enumerate(s):
            if c==s[0] and i and n%i==0 and s==s[:i]*(n//i):
                return True
        return False