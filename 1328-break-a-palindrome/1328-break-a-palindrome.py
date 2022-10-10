class Solution:
    def breakPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:return ""
        s=list(s)
        for i in range(n//2):
            if s[i]!='a':
                s[i]='a'
                return "".join(s)
        s[-1]="b"
        return "".join(s)
        