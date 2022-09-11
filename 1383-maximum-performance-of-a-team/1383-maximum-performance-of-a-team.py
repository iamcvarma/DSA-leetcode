class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr=sorted(list(zip(efficiency,speed)),reverse = 1)
        heap=[]
        mod= 1000000007
        ma,curr=0,0
        for ef,sp in arr:
            heapq.heappush(heap,sp)
            curr+=sp
            if len(heap)>k:
                curr-=heapq.heappop(heap)
            ma=max(ma,curr*ef)
        return ma%mod