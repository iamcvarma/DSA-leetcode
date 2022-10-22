class Solution:
    def longestPalindrome(self, s: str) -> str:
        def solve(i,j):
            while i>-1 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return i,j
        mi,mj=0,0
        for k in range(len(s)):
            i,j = solve(k,k)
            if j-i-1>mj-mi-1:
                mi,mj = i,j
            i,j = solve(k,k+1)    
            if j-i-1>mj-mi-1:
                mi,mj = i,j
        return s[mi+1:mj]