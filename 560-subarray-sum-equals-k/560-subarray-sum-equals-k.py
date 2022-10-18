class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        
        d=defaultdict(int)
        d[0]=1
        res=0
        for n in nums:
            res+=d[n-k]
            d[n]+=1
        return res