class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        for i in range(2,len(nums)):
            a=0
            b=i-1
            while a<b:
                if nums[a]+nums[b]>nums[i]:
                    res+=b-a
                    b-=1
                else:a+=1
        return res