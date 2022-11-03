class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        bucket = [""]*(len(s)+1)
        for c,f in freq.items():
            bucket[f]+=c
        res=[]
        for i in range(len(s),0,-1):
            if bucket[i]:
                for c in bucket[i]:
                    res.append(c*i)
        return ''.join(res)