class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0]+[inf]*(days[-1])
        j=0
        for i in range(1,len(dp)):
            if i!=days[j]:
                dp[i]=dp[i-1]
                continue
            dp[i]=min(dp[i],costs[0]+dp[max(i-1,0)])
            dp[i]=min(dp[i],costs[1]+dp[max(i-7,0)])
            dp[i]=min(dp[i],costs[2]+dp[max(i-30,0)])
            j+=1
        return dp[-1]