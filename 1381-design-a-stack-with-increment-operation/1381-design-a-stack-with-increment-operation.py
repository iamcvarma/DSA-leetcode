class CustomStack:

    def __init__(self, maxSize: int):
        self.st=[]
        self.n = maxSize
        return None

    def push(self, x: int) -> None:
        if len(self.st)==self.n:return
        self.st.append((x,0))
        return
    
    def pop(self) -> int:
        if not self.st:return -1
        top,off = self.st.pop()
        if self.st:
            x,y = self.st.pop()
            self.st.append((x,y+off))
        return top+off

    def increment(self, k: int, val: int) -> None:
        if not self.st:return
        k = min(k,len(self.st))-1
        self.st[k] = (self.st[k][0],self.st[k][1]+val)
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)