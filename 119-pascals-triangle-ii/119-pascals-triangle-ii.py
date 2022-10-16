class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr=[1]
        for i in range(rowIndex):
            new=[1]*(len(arr)+1)
            for j in range(1,len(arr)):
                new[j]=arr[j-1]+arr[j]
            arr=new
        return arr