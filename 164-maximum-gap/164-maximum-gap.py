class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        mi,ma,n = min(nums),max(nums),len(nums)
        interval = math.ceil((ma-mi)/(n-1))
        minbucket = [inf]*(n-1)
        maxbucket = [-inf]*(n-1)
        res = 0
        for num in nums:
            if num==mi or num==ma:continue
            i = (num-mi)//(interval)
            minbucket[i] = min(minbucket[i],num)
            maxbucket[i] = max(maxbucket[i],num)
        
        pre = mi
        for i in range(n-1):
            if minbucket[i]==inf:continue
            res = max(res,minbucket[i]-pre)
            pre = maxbucket[i]
        res = max(res,ma-pre)
        return res