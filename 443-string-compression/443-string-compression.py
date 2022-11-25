class Solution:
    def compress(self, arr: List[str]) -> int:
        def add():
            nonlocal i
            arr[i]=curr
            i+=1
            if count>1:
                for c in str(count):
                    arr[i]=c
                    i+=1
        i=0
        count=1
        curr = arr[0]
        for j in range(1,len(arr)):
            if arr[j-1]==arr[j]:
                count+=1
            else:
                add()
                curr = arr[j]
                count=1
        add()
        return i
        