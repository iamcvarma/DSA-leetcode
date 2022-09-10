class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi, res = inf, 0
        for n in prices:
            res= max(res, n-mi)
            mi= min(mi, n)
        return res