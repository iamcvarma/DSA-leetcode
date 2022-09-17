class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d= {}
        for i,w in enumerate(words):d[w[::-1]] = i
        
        res = set()
        
        for i,word in enumerate(words):
            for k in range(len(word)+1):
                pre = word[:k]
                post = word[k:]
                
                if pre in d and d[pre]!=i and post==post[::-1]:res.add((i,d[pre]))
                
                if post in d and d[post]!=i and pre==pre[::-1]:res.add((d[post],i))
        
        return [list(pair) for pair in res]