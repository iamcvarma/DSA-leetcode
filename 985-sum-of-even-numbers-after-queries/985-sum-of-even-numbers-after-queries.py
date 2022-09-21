class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = reduce(lambda a,b:a if b&1 else a+b,nums,0)
        res =[]
        for v,i in queries:
            if nums[i]%2==0:
                even-=nums[i]
            nums[i]+=v
            if nums[i]%2==0: even+=nums[i]
            res.append(even)
        return res