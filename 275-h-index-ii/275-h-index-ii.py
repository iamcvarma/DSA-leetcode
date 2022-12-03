class Solution:
    def hIndex(self, arr: List[int]) -> int:
        n = len(arr)
        s,e = 0,n-1
        while s<=e:
            m = s+e>>1
            if (n-m)<=arr[m]:
                e=m-1
            else:
                s=m+1
        return n-s