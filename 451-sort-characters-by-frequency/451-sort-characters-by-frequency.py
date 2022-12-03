class Solution:
    def frequencySort(self, s: str) -> str:
        cc =Counter(s)
        arr = sorted(cc.keys(),key = lambda x:(-cc[x],x))
        res=[]
        for c in arr:
            res.extend([c]*cc[c])
        return res