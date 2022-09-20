class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        arr =[inf]*32
        for j in range(len(nums)-1,-1,-1):
            i=0
            while (1<<i)<=nums[j]:
                if (1<<i)&nums[j]:
                    arr[i] = j
                i+=1
            temp = 0
            for n in arr:
                if n<inf:temp = max(temp,n)
            nums[j] = (temp or j)-j+1
            
        return nums