class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        curr = 0
        ma = 0
        for j in range(len(nums)):
            curr+=nums[j]
            while nums[j]*(j-i+1)-curr>k:
                curr-=nums[i]
                i+=1
            ma = max(ma, j-i+1)
        return ma
        