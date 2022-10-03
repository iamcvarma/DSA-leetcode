class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i=res=0
        n=len(colors)
        while i<n:
            curr=colors[i]
            total,ma=0,0
            while i<n and curr==colors[i]:
                total+=neededTime[i]
                ma=max(ma,neededTime[i])
                i+=1
            res+=total-ma
        return res