class Solution:
    def countPalindromes(self, s: str) -> int:
        res,n = 0,len(s)
        prefix,pre = [[[0]*10 for _ in range(10)] for __ in range(n)],[0]*10
        suffix,suf = [[[0]*10 for _ in range(10)] for __ in range(n)],[0]*10

        for i in range(n):
            curr = int(s[i])
            if i:
                for x in range(10):
                    for y in range(10):
                        prefix[i][x][y] = prefix[i-1][x][y]
                        if curr==y: prefix[i][x][y]+=pre[x]
            pre[curr]+=1
        
        for i in range(n-1,-1,-1):
            curr = int(s[i])
            if i<n-1:
                for x in range(10):
                    for y in range(10):
                        suffix[i][x][y] = suffix[i+1][x][y]
                        if curr==y: suffix[i][x][y]+=suf[x]
            suf[curr]+=1
        for i in range(2,n-2):
            for x in range(10):
                for y in range(10):
                    res+= prefix[i-1][x][y]*suffix[i+1][x][y]
        
        return res%1000000007
            