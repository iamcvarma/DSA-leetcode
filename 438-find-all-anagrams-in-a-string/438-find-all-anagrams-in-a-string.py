class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        i = 0
        n = len(p)
        res = []
        curr = defaultdict(int)
        
        def check(a,b):
            for c in b:
                if b[c]!=a[c]:return False
            return True
        
        for j in range(len(s)):
            curr[s[j]]+=1
            if j>=n:
                curr[s[i]]-=1
                i+=1
            if check(curr,target):
                res.append(i)
        return res
                