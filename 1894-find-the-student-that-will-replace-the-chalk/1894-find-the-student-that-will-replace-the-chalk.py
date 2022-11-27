class Solution:
    def chalkReplacer(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        k %=nums[-1]
        return bisect.bisect_right(nums,k)