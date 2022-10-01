from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        d = SortedList()
        res=0
        for i in range(len(nums1)):
            k = nums1[i]-nums2[i]
            res+=d.bisect_left(k+diff+1)
            d.add(k)
        return res
                