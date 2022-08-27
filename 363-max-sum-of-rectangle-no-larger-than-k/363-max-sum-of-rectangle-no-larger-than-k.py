class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def find(arr,target):
            res=-inf
            tree=[0]
            pre=0
            for n in arr:
                pre+=n
                i=bisect.bisect_left(tree,pre-target)
                if i<len(tree):res=max(res,pre-tree[i])
                bisect.insort(tree,pre)
            return res
        m,n=len(matrix),len(matrix[0])
        ans=-inf
        for i in range(m):
            temp=[0]*n
            for j in range(i,m):
                for c in range(n):temp[c]+=matrix[j][c]
                ans=max(ans,find(temp,k))
                if ans==k:return ans
        return ans