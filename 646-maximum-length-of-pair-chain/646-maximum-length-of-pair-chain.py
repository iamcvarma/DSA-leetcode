class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        count=0
        ma=-inf
        for i in range(len(pairs)):
            if pairs[i][0]>ma:
                ma=pairs[i][1]
                count+=1
        return count