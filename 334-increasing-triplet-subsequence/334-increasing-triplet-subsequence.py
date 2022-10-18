class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a,b = inf , inf
        for n in nums:
            if n<=a:
                a = n
            elif n<=b:
                b = n
            else:
                return True
        return False