class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.arr=[[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key%self.size
        for i,pair in enumerate(self.arr[idx]):
            if pair[0]==key:
                self.arr[idx][i][1]=value
                return
        self.arr[idx].append([key,value])

    def get(self, key: int) -> int:
        i = key%self.size
        for k,v in self.arr[i]:
            if k==key:return v
        return -1

    def remove(self, key: int) -> None:
        idx = key%self.size
        for i,pair in enumerate(self.arr[idx]):
            if pair[0]==key:
                self.arr[idx][i],self.arr[idx][-1]=self.arr[idx][-1],self.arr[idx][i]
                self.arr[idx].pop()
        return
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)