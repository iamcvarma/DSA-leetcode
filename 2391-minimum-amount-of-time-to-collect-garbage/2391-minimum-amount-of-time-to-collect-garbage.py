class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m,p,g,res=0,0,0,0
        arr=[0]
        for n in travel:
            arr.append(arr[-1]+n)

        for i,s in enumerate(garbage):
            x,y,z=s.count('M'),s.count('P'),s.count('G')
            if x:m+=arr[i]-m
            if y:p+=arr[i]-p
            if z:g+=arr[i]-g
            res+=x+y+z
        return res+m+p+g