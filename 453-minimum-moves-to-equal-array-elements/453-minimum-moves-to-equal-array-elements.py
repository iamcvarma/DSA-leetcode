class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mi = nums[0]
        res = 0
        for i,v in enumerate(nums):
            if v<mi:
                res+=i*(mi-v)
                mi=v
            res+=v-mi
        return res