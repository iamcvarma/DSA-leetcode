class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n  = len(nums)
        presum =[0]*(n+1)
        for i in range(1,n+1):presum[i] = presum[i-1]+nums[i-1]
        res = inf
        q = deque([])
        for i in range(n+1):
            while q and presum[q[-1]]>=presum[i]:q.pop()
            while q and presum[i]-presum[q[0]]>=k:
                res=min(res,i-q.popleft())
            q.append(i)
        return -1 if res==inf else res
            