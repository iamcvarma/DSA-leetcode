class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s,f = nums[0],nums[nums[0]]
        while s!=f:
            s = nums[s]
            f = nums[nums[f]]
        f = 0
        while s!=f:
            s = nums[s]
            f = nums[f]
        return s