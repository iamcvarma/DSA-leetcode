class Solution:
    def longestPalindrome(self, s: str) -> int:
        mid=0
        res=0
        for i,v in Counter(s).items():
            if v&1:mid=1
            res+=(v//2)*2
        return res+mid