class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def solve(i,j):
            if i>=j:return 0
            if (i,j) in dp:return dp[(i,j)]
            ans=inf
            for k in range(i,j):
                left=solve(i,k)
                right=solve(k+1,j)
                ans=min(ans,left+right+(max(arr[i:k+1])*max(arr[k+1:j+1])))
            dp[(i,j)]=ans
            return ans
        dp={}
        return solve(0,len(arr)-1)
                