class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(' ')
        if len(arr)!=len(pattern):return False
        d,e = {},{}
        for c,word in zip(pattern,arr):
            if (c in d and d[c]!=word) or word in e and e[word]!=c:return False
            else: 
                d[c] = word
                e[word] = c
        return True