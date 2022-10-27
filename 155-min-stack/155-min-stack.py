class MinStack:

    def __init__(self):
        self.st=[]

    def push(self, val: int) -> None:
        curr_min = min(val,self.getMin())
        self.st.append((val,curr_min))
        

    def pop(self) -> None:
        if self.st: self.st.pop()

    def top(self) -> int:
        if self.st: return self.st[-1][0]

    def getMin(self) -> int:
        if self.st:
            return self.st[-1][1]
        return inf

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()