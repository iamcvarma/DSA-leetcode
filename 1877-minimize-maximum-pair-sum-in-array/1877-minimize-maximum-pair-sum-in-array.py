class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i]+nums[~i] for i in range(len(nums)//2+1))
        