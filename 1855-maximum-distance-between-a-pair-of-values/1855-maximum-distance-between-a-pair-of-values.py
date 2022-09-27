class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def binary(s,e,target):
            while s<e:
                m = s+e>>1
                if nums1[m]<=target:
                    e=m
                else:
                    s=m+1
            return e
        ma = 0
        n = len(nums1)-1
        for i in range(len(nums2)):
            j = min(i,n)
            if nums2[i]>=nums1[j]:
                ma = max(ma,i-binary(0,j,nums2[i]))
        return ma