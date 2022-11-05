#kmp
class Solution:
    def strStr(self, s: str, p: str) -> int:
        def getLPS(p):
            m = len(p)
            lps = [0]*m
            i,j=1,0
            while i<m:
                if p[i]==p[j]:
                    lps[i] = j+1
                    i+=1
                    j+=1
                else:
                    if j:
                        j = lps[j-1]
                    else:
                        i+=1
            return lps
        
        m,n = len(p),len(s)
        lps = getLPS(p)
        i,j=0,0
        while i<n:
            if s[i]==p[j]:
                i+=1
                j+=1
            else:
                if j:
                    j=lps[j-1]
                else:
                    i+=1
            if j==m:
                return i-j
        return -1