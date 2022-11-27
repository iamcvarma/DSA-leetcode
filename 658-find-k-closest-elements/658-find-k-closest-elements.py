class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        j = bisect.bisect_right(arr,x)
        i=j-1
        while j-i-1<k:
            left = arr[i] if i>-1 else -inf
            right = arr[j] if j<len(arr) else inf
            if abs(left-x)<abs(right-x):
                i-=1
            elif abs(left-x)==abs(right-x):
                i-=1
            else:
                j+=1
        return arr[i+1:j]
                
            