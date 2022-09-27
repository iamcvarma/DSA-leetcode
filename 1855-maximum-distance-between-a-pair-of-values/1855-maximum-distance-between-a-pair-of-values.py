class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        ma = i = j = 0
        while i<n and j<m:
            if nums1[i]>nums2[j]:
                i+=1
            else:
                ma = max(ma,j-i)
                j+=1
        return ma