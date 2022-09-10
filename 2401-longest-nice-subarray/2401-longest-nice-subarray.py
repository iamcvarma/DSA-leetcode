class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i=curr=ma=0
        for j in range(len(nums)):
            while curr&nums[j]!=0:
                curr=curr^nums[i]
                i+=1
            curr|=nums[j]
            ma=max(ma,j-i+1)
        return ma