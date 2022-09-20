class Solution:
    def findLength(self, a: List[int], b: List[int]) -> int:
        m,n = len(a),len(b)
        dp  = [[0]*(n+1) for _ in range(m+1)] 
        pre = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if a[i-1]==b[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                
            
        return max((max(r) for r in dp))