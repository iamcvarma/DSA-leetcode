class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def bisect(arr,target):
            s,e = 0,len(arr)-1
            while s<e:
                m = s+e+1>>1
                if arr[m]<=target:
                    s=m
                else:
                    e=m-1
            return s
        i = bisect(arr,x)
        j=i+1
        while k:
            if i<0:
                j+=1
            elif j>len(arr)-1:
                i-=1
            else:
                if abs(arr[i]-x)<=abs(arr[j]-x):
                    i-=1
                else:
                    j+=1
            k-=1
                
        return arr[i+1:j]