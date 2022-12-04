class Solution:
    def maxFrequency(self, nums: List[int], curr: int) -> int:
        nums.sort()
        ma=i=0
        for j in range(len(nums)):
            curr+=nums[j]
            while curr<nums[j]*(j-i+1):
                curr-=nums[i]
                i+=1
            ma = max(ma,j-i+1)
        return ma