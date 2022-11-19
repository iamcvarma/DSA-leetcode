class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(a,b,c):
            ax,ay = a
            bx,by = b
            cx,cy = c
            
            return (bx-ax)*(cy-ay)-(cx-ax)*(by-ay)
        
        points = sorted(trees)
        
        lower = []
        upper = []
        
        for point in points:
            while len(lower)>1 and cross(lower[-2],lower[-1],point)>0:
                lower.pop()
            lower.append(tuple(point))
            
            while len(upper)>1 and cross(upper[-2],upper[-1],point)<0:
                upper.pop()
            upper.append(tuple(point))
        
        return list(set(upper+lower))
            