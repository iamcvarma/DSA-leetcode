class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        curr,n = sum(set(nums)),len(nums)
        return [sum(nums)-curr,(n*(n+1))//2-curr]
            