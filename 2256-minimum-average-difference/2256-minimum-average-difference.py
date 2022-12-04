class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pre,suf,res,mi,n = 0,sum(nums),0,inf,len(nums)
        for i,v in enumerate(nums):
            pre,suf = pre+v,suf-v
            post = 0
            if i<n-1: post = suf//(n-i-1)
            avg = abs((pre//(i+1))-post)
            if avg<mi: mi,res = avg,i
        return res
            