class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res=i=0
        curr=1
        for j in range(len(nums)):
            curr*=nums[j]
            while i<=j and curr>=k:
                curr//=nums[i]
                i+=1
            res+=j-i+1
        return res