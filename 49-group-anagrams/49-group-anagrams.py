class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for s in strs:
            h["".join(sorted(s))].append(s)
        return h.values()