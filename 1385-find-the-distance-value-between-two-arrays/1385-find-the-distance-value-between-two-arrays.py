class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        arr2.sort()
        for n in arr1:
            s,e=0,len(arr2)
            while s<e:
                m = s+e>>1
                if arr2[m]>=n:
                    e=m
                else:
                    s=m+1
            low = arr2[s-1] if s else -inf
            high = arr2[s] if s<len(arr2) else inf
            if low<n-d and n+d<high:res+=1
        return res