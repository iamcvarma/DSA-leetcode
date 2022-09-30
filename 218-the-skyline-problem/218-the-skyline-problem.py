class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        arr = [(l,-h,r) for l,r,h in buildings] + [(r,0,0) for l,r,h in buildings]
        arr.sort()
        
        res=[[0,0]]
        heap = [(0,inf)]
        
        for l,h,r in arr:
            while l>=heap[0][1]:
                heapq.heappop(heap)
            if h: heapq.heappush(heap,(h,r))
            
            if res[-1][1]!=-heap[0][0]:
                res.append([l,-heap[0][0]])
        return res[1:]