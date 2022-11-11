class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        T=F=0
        ma=i=0
        for j in range(len(s)):
            if s[j]=='T':T+=1
            else: F+=1
            while min(T,F)>k:
                if s[i]=='T':
                    T-=1
                else:F-=1
                i+=1
            ma=max(ma,j-i+1)
        return ma