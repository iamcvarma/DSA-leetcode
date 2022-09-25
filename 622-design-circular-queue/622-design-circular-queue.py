class MyCircularQueue:

    def __init__(self, k: int):
        self.n = k
        self.q = [0]*k
        self.f,self.r=-1,-1
        return None

    def enQueue(self, value: int) -> bool:
        if self.isFull():return False
        if self.isEmpty():self.r=0
        self.f = (self.f+1)%self.n
        self.q[self.f]=value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():return False
        if self.r==self.f:
            self.r=self.f=-1
        else:
            self.r = (self.r+1)%self.n
        return True
    def Front(self) -> int:
        if self.isEmpty():return -1
        return self.q[self.r]

    def Rear(self) -> int:
        if self.isEmpty():return -1
        return self.q[self.f]

    def isEmpty(self) -> bool:
        return self.f==-1

    def isFull(self) -> bool:
        return (self.f+1)%self.n==self.r


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()