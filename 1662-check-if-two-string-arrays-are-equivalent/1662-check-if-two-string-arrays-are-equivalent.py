class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a=b=c=d=0
        while a<len(word1) and b<len(word2):
            if word1[a][c]!=word2[b][d]:return False
            c+=1
            if c>=len(word1[a]):
                c=0
                a+=1
            d+=1
            if d>=len(word2[b]):
                d=0
                b+=1
        return a==len(word1) and b==len(word2)