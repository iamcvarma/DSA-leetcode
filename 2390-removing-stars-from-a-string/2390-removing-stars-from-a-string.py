class Solution:
    def removeStars(self, s: str) -> str:
        count=0
        res=""
        for c in s[::-1]:
            if c=='*':
                count+=1
            elif count:
                count-=1
            else:
                res=c+res
        return res