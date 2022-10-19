class WordWrap:
    def __init__(self,word):
        self.word = word
        return 
    
    def __lt__(self,other):
        return self.word>other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        arr = [(freq,word) for word,freq in freq.items()]
        heap=[]
        for freq,word in arr:
            heapq.heappush(heap,(freq,WordWrap(word)))
            if len(heap)>k:
                heapq.heappop(heap)
    
        res=[]
        while heap:
            res.append(heapq.heappop(heap)[1].word)
        return res[::-1]