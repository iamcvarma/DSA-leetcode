class MyCalendar:

    def __init__(self):
        self.arr=[]

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self.arr,end-1,key = lambda x:x[0])
        if i<1:
            self.arr = [(start,end-1)]+self.arr
            return True
        pre = self.arr[i-1]
        if max(start,pre[0])<=min(end-1,pre[1]):return False
        self.arr = self.arr[:i]+[(start,end-1)]+self.arr[i:]
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)