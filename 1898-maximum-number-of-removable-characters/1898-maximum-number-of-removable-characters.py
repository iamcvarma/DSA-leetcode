class Solution:
    def maximumRemovals(self, s: str, p: str, arr: List[int]) -> int:
        def check(seen):
            j=0
            for i in range(len(s)):
                if i in seen:continue
                if p[j]==s[i]:
                    j+=1
                    if j==len(p):
                        return True
            return False
        
        start ,end = 0,len(arr)
        while start<end:
            mid = start+end+1>>1
            if check(set(arr[:mid])):
                start=mid
            else:
                end = mid-1
                
        return start
                