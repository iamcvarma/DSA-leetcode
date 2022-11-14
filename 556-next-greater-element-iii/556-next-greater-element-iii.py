class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))
        
        i = len(arr)-1
        while i and arr[i]<=arr[i-1]: 
            i-=1
        if not i:return -1
        
        j = i
        while j<len(arr) and arr[j]>arr[i-1]:
            j+=1
        arr[i-1],arr[j-1] = arr[j-1],arr[i-1]
        arr[i:] = reversed(arr[i:])
        
        ans = int("".join(arr))
        if 1<=ans<=(2**31-1):
            return ans
        
        return -1