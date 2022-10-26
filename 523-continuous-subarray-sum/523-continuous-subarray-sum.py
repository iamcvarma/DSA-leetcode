class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre=[0]
        for n in nums: pre.append(pre[-1]+n)
        
        hmap ={}
        for i,v in enumerate(pre):
            if v%k in hmap:
                if hmap[v%k]!=i-1:
                    return True
            else:
                hmap[v%k]=i
        return False