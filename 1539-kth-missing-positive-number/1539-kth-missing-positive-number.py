class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s,e = 0,len(arr)-1
        while s<e:
            m = s+e>>1
            if arr[m]-(m+1)>=k:
                e= m
            else : s=m+1
        
        res = arr[e]-((arr[e]-(e+1))-k)-1
        if res>=arr[-1]:res+=1
        return res