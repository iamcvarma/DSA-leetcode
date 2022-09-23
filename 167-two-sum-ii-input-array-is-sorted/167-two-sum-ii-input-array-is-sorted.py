class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        def bsearch(s,e,target):
            while s<=e:
                m = s+e>>1
                if arr[m]>target:
                    e=m-1
                elif arr[m]<target:
                    s=m+1
                else:return m
            return -1
        n = len(arr)-1
        for i,v in enumerate(arr):
            res = bsearch(i+1,n,target-v)
            if res!=-1:return [i+1,res+1]
        