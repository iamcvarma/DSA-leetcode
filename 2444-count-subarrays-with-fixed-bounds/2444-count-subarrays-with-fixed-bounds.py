class Solution:
    def countSubarrays(self, nums: List[int], a: int, b: int) -> int:
        ma,mi = -1,-1
        res=0
        i,j = 0,0
        n = len(nums)
        while j<n:
            if not (a<=nums[j]<=b):
                i=j+1
            if nums[j]==a:
                mi=j
            if nums[j]==b:
                ma = j
            res+=max(0,min(mi,ma)-i+1)
            j+=1
            
        return res
        