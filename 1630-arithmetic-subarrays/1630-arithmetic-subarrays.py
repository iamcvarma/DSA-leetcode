class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            diff = arr[1]-arr[0]
            for i in range(1,len(arr)-1):
                if arr[i+1]-arr[i]!=diff:return False
            return True
        return [check(sorted(nums[i:j+1])) for i,j in zip(l,r)]