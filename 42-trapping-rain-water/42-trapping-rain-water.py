class Solution:
    def trap(self, arr: List[int]) -> int:
        left,right = 0,len(arr)-1
        leftmax=rightmax=0
        res=0
        while left<=right:
            if leftmax<rightmax:
                leftmax=max(leftmax,arr[left])
                res+=leftmax-arr[left]
                left+=1
            else:
                rightmax=max(rightmax,arr[right])
                res+=rightmax-arr[right]
                right-=1
        return res