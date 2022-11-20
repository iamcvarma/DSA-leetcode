class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i):
                for k in range(j):
                    if len(set([nums[i],nums[j],nums[k]]))==3:
                        res+=1
        return res