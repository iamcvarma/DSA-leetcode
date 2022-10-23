class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            curr = 0
            for j in range(i,n):
                curr=math.gcd(curr,nums[j])
                if curr==k:res+=1
                elif curr<k:break
        return res