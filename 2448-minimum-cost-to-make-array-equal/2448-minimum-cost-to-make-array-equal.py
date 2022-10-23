class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        res=0
        nums = sorted(zip(nums,cost))
        total = sum(cost)//2
        for num,cost in nums:
            res+=cost
            if res>total:
                mid = num
                break
        return sum(abs(mid-n)*c for n,c in nums)