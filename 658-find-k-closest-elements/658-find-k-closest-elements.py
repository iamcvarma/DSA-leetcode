class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        s,e = 0,len(arr)-k
        while s<e:
            m = s+e>>1
            if x-arr[m]>arr[m+k]-x:
                s=m+1
            else:
                e=m
        return arr[s:s+k]
            