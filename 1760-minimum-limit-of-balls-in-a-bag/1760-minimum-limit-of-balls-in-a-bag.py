class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(ma):
            curr=0
            for n in nums:
                curr+=ceil(n/ma)-1
                if curr>maxOperations:
                    return False
            return True
        s,e = 1,max(nums)
        while s<e:
            m = s+e>>1
            if check(m):
                e=m
            else:
                s=m+1
        return e