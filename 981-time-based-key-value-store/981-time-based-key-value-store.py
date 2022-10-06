class TimeMap:

    def __init__(self):
        self.ds=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        arr=self.ds[key]
        if not arr or arr[0][0]>timestamp:return ""
        s,e=0,len(arr)-1
        while s<e:
            m= s+e+1>>1
            if arr[m][0]<=timestamp:
                s=m
            else:
                e=m-1
        return arr[s][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)