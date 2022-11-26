class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in range(len(nums)):
            for j in range(i):
                right=bisect.bisect_left(nums,(nums[i]+nums[j]),lo=i)
                if right<=i:continue
                res+=right-i-1
        return res