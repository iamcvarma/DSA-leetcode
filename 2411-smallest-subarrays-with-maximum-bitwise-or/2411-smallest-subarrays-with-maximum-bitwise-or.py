class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        arr =[0]*32
        for j in range(len(nums)-1,-1,-1):
            i=0
            while (1<<i)<=nums[j]:
                if (1<<i)&nums[j]:
                    arr[i] = j
                i+=1
            nums[j] = max(max(arr)-j+1,1)
        return nums