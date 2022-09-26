class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a= Counter(nums1)
        b = Counter(nums2)
        res=[]
        for c in a:
            if c in b:
                res.extend([c]*min(a[c],b[c]))
        return res