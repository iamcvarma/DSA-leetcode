class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pre={}
        for i,v in enumerate(nums):
            if v in pre and i-pre[v]<=k:
                return True
            pre[v] = i
        return False