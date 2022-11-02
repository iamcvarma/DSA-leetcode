class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l,r = 0,len(nums)-1
        k= len(nums)-k
        def quickSelect(l,r,k):
            p=l
            for i in range(l,r):
                if nums[i]<nums[r]:
                    nums[p],nums[i]=nums[i],nums[p]
                    p+=1
            nums[p],nums[r]=nums[r],nums[p]
            if k<p:
                return quickSelect(l,p-1,k)
            elif k>p:
                return quickSelect(p+1,r,k)
            else:
                return nums[p]
        return quickSelect(l,r,k)