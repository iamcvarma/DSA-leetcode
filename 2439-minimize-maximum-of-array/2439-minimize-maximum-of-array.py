class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr,res=0,0
        for i,n in enumerate(nums,1):
            curr+=n
            res=max(res,math.ceil(curr/i))
        return res