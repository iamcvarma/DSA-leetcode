class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d=defaultdict(int)
        for arr in wall:
            pre=0
            for n in arr[:-1]:
                pre+=n
                d[pre]+=1
        return len(wall)-max(d.values(),default=0)