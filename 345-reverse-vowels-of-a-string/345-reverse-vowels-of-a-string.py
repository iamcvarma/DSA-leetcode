class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vvls = "aeiouAEIOU"
        i,j=0,len(s)-1
        while i<j:
            while i<j and s[i] not in vvls:
                i+=1
            while j>i and s[j] not in vvls:
                j-=1
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        return "".join(s)