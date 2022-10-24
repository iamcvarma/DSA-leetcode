class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def mask(word):
            res= 0
            for c in word:
                res|=(1<<ord(c)-ord('a'))
            return res
        comb = [0]
        for word in arr:
            if len(word)!=len(set(word)):continue
            m = mask(word)
            for n in comb:
                if not m&n:comb.append(m|n)
            
        
        return max(i.bit_count() for i in comb)