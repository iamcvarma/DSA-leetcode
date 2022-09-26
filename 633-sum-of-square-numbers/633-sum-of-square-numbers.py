class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = [i*i for i in range(int(c**0.5+1))]
        i,j=0,len(arr)-1
        while i<=j:
            if arr[i]+arr[j]>c:
                j-=1
            elif arr[i]+arr[j]<c:
                i+=1
            else:
                return True
        return False