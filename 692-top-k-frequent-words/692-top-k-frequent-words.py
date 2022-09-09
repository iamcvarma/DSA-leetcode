class Freq_obj:
    def __init__(self,word,freq):
        self.word=word
        self.freq=freq
        
    def __lt__(self,other):
        if self.freq!=other.freq:
            return self.freq<other.freq
        else:
            return self.word>other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap,res=[],[]
        for word, freq in Counter(words).items():
            if len(heap)<k:
                heapq.heappush(heap,Freq_obj(word,freq))
            else:
                heapq.heappushpop(heap,Freq_obj(word,freq))
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]