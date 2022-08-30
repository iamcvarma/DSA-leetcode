class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res=0
        while len(arr)>1:
            i=arr.index(min(arr))
            mul=min(arr[i-1],arr[i+1]) if 0<i<len(arr)-1 else (arr[i-1] if i else arr[i+1])
            res+=arr[i]*mul
            arr.pop(i)
        return res