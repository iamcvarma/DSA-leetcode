class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k>1:
            return "".join(sorted(s))
        mi = s
        for i in range(len(s)):
            mi = min(mi,s[i:]+s[:i])
        return mi