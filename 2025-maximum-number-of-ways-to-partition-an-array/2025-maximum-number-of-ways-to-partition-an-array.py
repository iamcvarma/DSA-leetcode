class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums))
        total = prefix[-1]
        res = 0
        if total % 2 == 0:
            res = prefix[:-1].count(total//2)
        
        right = Counter(total-(2*pre) for pre in prefix[:-1])
        left = Counter()
        res = max(res,right[k-nums[0]])
        
        for i in range(1,len(nums)):
            diff = total-2*prefix[i-1]
            right[diff]-=1
            left[diff]+=1
            res = max(res,left[nums[i]-k]+right[k-nums[i]])
        return res