class MedianFinder:

    def __init__(self):
        self.left,self.right = [],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left,-num)
        if self.right and self.right[0]<-self.left[0]:
            heapq.heappush(self.right,-heapq.heappop(self.left))
        if abs(len(self.left)-len(self.right))>1:
            if len(self.left)>len(self.right):
                heapq.heappush(self.right,-heapq.heappop(self.left))
            else:
                heapq.heappush(self.left,-heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left)==len(self.right):
            return (-self.left[0]+self.right[0])/2
        if len(self.left)>len(self.right):
            return -self.left[0]
        return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()