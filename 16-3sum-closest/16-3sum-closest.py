class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res=40000
        nums.sort()
        n=len(nums)
        if sum(nums[:3])>=target:
            return sum(nums[:3])
        if sum(nums[-3:])<target:
            return sum(nums[-3:])
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                curr=nums[i]+nums[l]+nums[r]
                if curr==target:return curr
                if abs(res-target)>abs(curr-target):
                    res=curr
                if curr>target:
                    r-=1
                else:l+=1
        return res
                