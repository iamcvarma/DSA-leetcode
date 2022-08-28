class Solution:
    def answerQueries(self, arr: List[int], queries: List[int]) -> List[int]:
        def bisect(target):
            if target<arr[0]:return 0
            s,e=0,len(arr)-1
            while s<e:
                m=s+e+1>>1
                if arr[m]<=target:
                    s=m
                else:
                    e=m-1
            return s+1
        arr.sort()
        for i in range(1,len(arr)):
            arr[i]+=arr[i-1]
        return list(map(bisect,queries))