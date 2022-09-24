class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bisect(arr,target):
            s,e = 0,len(arr)
            while s<e:
                m = s+e>>1
                if arr[m]<=target:
                    e= m
                else:
                    s= m+1
            return e
        res = 0
        for arr in grid:
            res+=len(grid[0])-bisect(arr,-1)
        return res