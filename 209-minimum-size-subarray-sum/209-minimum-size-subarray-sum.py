class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def bsearch(s,e,target):
            while s<e:
                m = s+e+1>>1
                if pre[m]<=target:
                    s = m
                else:
                    e = m-1
            return s
        n =len(nums)
        res=inf
        pre = [0]*(n+1)
        for i in range(n):
            pre[i+1] = pre[i]+nums[i]
        for i in range(n+1):
            if pre[i]<target:continue
            index = bsearch(0,i,pre[i]-target)
            res=min(res,i-index)
        return 0 if res==inf else res
            
        