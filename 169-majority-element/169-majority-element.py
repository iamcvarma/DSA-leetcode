class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=curr=1
        for n in nums:
            if n==curr:
                count+=1
            elif count==1:
                curr=n
            else:
                count-=1
        return curr