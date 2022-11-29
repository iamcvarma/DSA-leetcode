class RandomizedSet:

    def __init__(self):
        self.seen = {}
        self.arr=[]

    def insert(self, val: int) -> bool:
        if val in self.seen:return False
        self.seen[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.seen:return False
        i = self.seen[val]
        self.arr[i],self.arr[-1] = self.arr[-1],self.arr[i]
        self.seen[self.arr[i]] = i
        del self.seen[self.arr.pop()]
        return True
        
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()