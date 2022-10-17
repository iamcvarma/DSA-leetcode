class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=0
        intervals.sort(key = lambda x:x[1])
        last = -inf
        for x,y in intervals:
            if x>=last:
                last = y
            else:
                res+=1
        return res