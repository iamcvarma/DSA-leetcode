class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        temp=nums[0]=nums[0]%k
        seen=set([0])
        for i in range(1,len(nums)):
            nums[i]= (nums[i-1]+nums[i])%k
            if nums[i] in seen: return True
            seen.add(temp)
            temp = nums[i]
        return False