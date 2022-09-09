class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        prop=sorted(properties,key=lambda x:(-x[0],x[1]))
        ma,res=-1,0
        for x,y in prop:
            if y<ma:res+=1
            else:ma=y
        return res