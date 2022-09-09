class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        hmap=defaultdict(list)
        for x, y in properties:
            hmap[x].append(y)
        
        ma,res=-1,0
        for d in sorted(hmap.keys(),reverse=True):
            temp=-1
            for y in hmap[d]:
                if y<ma:res+=1
                temp=max(temp,y)
            ma=max(ma,temp)
        return res