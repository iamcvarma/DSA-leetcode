class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s,e = 0,len(arr)-1
        while s<e:
            m = s+e>>1
            if arr[m]>arr[m+1]:
                e=m
            else:
                s=m+1
        return s