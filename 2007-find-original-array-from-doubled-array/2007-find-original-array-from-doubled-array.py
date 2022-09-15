class Solution:
    def findOriginalArray(self, arr: List[int]) -> List[int]:
        if len(arr)&1:return []
        cc =Counter(arr)
        res=[]
        for n in sorted(cc):
            if 2*n in cc and cc[2*n]:
                cc[2*n]-=cc[n] if n else cc[n]//2
                res.extend([n]*cc[n])
                cc[n]=0
        if any(cc.values()):return []
        return res