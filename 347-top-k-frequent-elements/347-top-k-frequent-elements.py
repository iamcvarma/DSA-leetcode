class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for c in freq:
            heapq.heappush(heap,(freq[c],c))
            if len(heap)>k:
                heapq.heappop(heap)
        return [b for a,b in heap]