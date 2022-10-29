class BIT:
    def __init__(self,n):
        self.arr = [0]*(n+1)
    
    def query(self,i):
        res = 0
        while i>0:
            res+= self.arr[i]
            i-= (i&(-i))
        return res
    def update(self,i,val):
        while i<len(self.arr):
            self.arr[i]+=val
            i+= (i&(-i))
        return

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n= len(nums1)
        pre,suf=[0]*n,[0]*n
        pos = {num:i for i,num in enumerate(nums2)}
        
        bit1,bit2 = BIT(n),BIT(n)

        for i in range(n):
            idx = pos[nums1[i]]
            pre[i]=bit1.query(idx)
            bit1.update(idx+1,1)
        
        for i in range(n-1,-1,-1):
            idx = pos[nums1[i]]
            suf[i] = (bit2.query(n)-bit2.query(idx))
            bit2.update(idx+1,1)
        res=0
        for i in range(n):
            res+=pre[i]*suf[i]
        return res
        