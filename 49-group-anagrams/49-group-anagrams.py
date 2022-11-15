class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)
        for word in strs:
            hmap["".join(sorted(word))].append(word)
        return hmap.values()