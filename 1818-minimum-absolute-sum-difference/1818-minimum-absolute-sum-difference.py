class Solution:
    def minAbsoluteSumDiff(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        arr = [abs(x-y) for x,y in zip(A,B)]
        A.sort()
        res=diff = sum(arr)
        for idx,v in enumerate(B):
            i = bisect.bisect_right(A,v)
            best = inf
            if -1<i<n: best =min(best,abs(A[i]-v))
            if -1<i-1<n:best = min(best,abs(A[i-1]-v))
            res = min(res,diff-arr[idx]+best)
        return res%(10**9+7)
        