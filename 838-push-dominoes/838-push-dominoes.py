class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        n =len(dom)
        force = [[float('inf'),float('inf')] for _ in range(n)]
        for i in range(n):
            if dom[i]=='R':
                j=i+1
                while j<n and dom[j]=='.':
                    force[j][0]=j-i
                    j+=1
            elif dom[i]=='L':
                j=i-1
                while j>-1 and dom[j]=='.':
                    force[j][1] = i-j
                    j-=1
        
        for i in range(n):
            if dom[i]!='.':continue
            x,y = force[i]
            if x>y:dom[i]='L'
            elif y>x:dom[i]='R'
        return "".join(dom)