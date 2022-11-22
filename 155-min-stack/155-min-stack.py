class MinStack:

    def __init__(self):
        self.st=[[-1,inf]]

    def push(self, val: int) -> None:
        self.st.append([val,min(self.st[-1][1],val)])

    def pop(self) -> None:
        return self.st.pop()[0]
        

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()