from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.arr=SortedList()
        return

    def book(self, start: int, end: int) -> int:
        self.arr.add((start,1))
        self.arr.add((end,0))
        ma=cur=0
        for x,y in self.arr:
            if y:cur+=1
            else:cur-=1
            ma=max(ma,cur)
        return ma


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)