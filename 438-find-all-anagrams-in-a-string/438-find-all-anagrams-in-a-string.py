class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def check(map1,map2):
            for c in map2:
                if map2[c]!=map1[c]:
                    return False
            return True
        
        
        n = len(p)
        i=0
        pattern = Counter(p)
        res=[]
        curr=Counter()
        for j in range(len(s)):
            curr[s[j]]+=1
            if j>=n:
                curr[s[i]]-=1
                i+=1
            if check(curr,pattern):
                res.append(i)
        return res
            