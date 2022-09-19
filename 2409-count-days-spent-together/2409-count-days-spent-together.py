class Solution:
    def countDaysTogether(self, p: str, q: str, r: str, s: str) -> int:
        
        months = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1,13): 
            months[i]+=months[i-1]
        
        arr = list(map(lambda x:x.split('-'),[p,q,r,s]))
        ax,ay,bx,by = list(map(lambda x: months[int(x[0])-1]+int(x[1]),arr))
        
        res =min(ay,by)-max(ax,bx)+1
        
        return res if res>-1 else 0