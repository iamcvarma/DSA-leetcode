import heapq as hq
class Solution:
    def totalCost(self, costs: List[int], k: int, cand: int) -> int:
        first,last = [],[]
        res=0
        n = len(costs)
        i,j = 0,n-1
        while k:
            while len(first)<cand and i<j:
                hq.heappush(first,(costs[i],i))
                i+=1
            while len(last)<cand and j>=i:
                hq.heappush(last,(costs[j],j))
                j-=1
            a = first[0][0] if first else inf
            b = last[0][0] if last else inf
            if a<=b:
                res+=a
                hq.heappop(first)
            else:
                res+=b
                hq.heappop(last)
            k=k-1
        return res
        