class Solution:
    def frequencySort(self, s: str) -> str:
        freq,res =Counter(s),""
        arr = sorted(freq.keys(), key = lambda x:-freq[x])
        for c in arr: res+=c*freq[c]
        return res