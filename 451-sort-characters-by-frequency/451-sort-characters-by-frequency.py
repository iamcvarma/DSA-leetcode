class Solution:
    def frequencySort(self, s: str) -> str:
        cc =Counter(s)
        return "".join(sorted(s,key = lambda x:(-cc[x],x)))