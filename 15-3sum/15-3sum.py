class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,n=[],len(nums)
        for i in range(n-2):
            if i and nums[i-1]==nums[i]:continue
            l,r=i+1,n-1
            while l<r:
                curr=nums[i]+nums[l]+nums[r]
                if curr<0:
                    l+=1
                elif curr>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
        return res