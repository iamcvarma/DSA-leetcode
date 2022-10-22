class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i=0
        res=[]
        hmap =defaultdict(int)
        for j in range(len(s)+1):
            if j>9:
                word = s[i:j]
                hmap[word]+=1
                if hmap[word]==2: res.append(word)
                i+=1
        return res
        