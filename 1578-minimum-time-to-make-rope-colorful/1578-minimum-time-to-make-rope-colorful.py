class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i=res=0
        n=len(colors)
        while i<n:
            heap = []
            curr=colors[i]
            while i<n and curr==colors[i]:
                heapq.heappush(heap,neededTime[i])
                i+=1
            while len(heap)>1:
                res+=heapq.heappop(heap)
        return res