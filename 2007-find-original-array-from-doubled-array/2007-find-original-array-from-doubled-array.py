class Solution:
    def findOriginalArray(self, arr: List[int]) -> List[int]:
        if len(arr)&1:return []
        hmap = {}
        res=[]
        arr.sort()
        for n in arr:
            if not n&1 and n//2 in hmap and hmap[n//2]:
                hmap[n//2]-=1
                res.append(n//2)
            else:hmap[n]= hmap.get(n,0)+1
        if any(hmap.values()):return []
        return res