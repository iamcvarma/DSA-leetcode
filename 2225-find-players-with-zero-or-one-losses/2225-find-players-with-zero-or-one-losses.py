class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = Counter(map(lambda x:x[0],matches))
        lose = Counter(map(lambda x:x[1],matches))
        return [sorted([i for i in win if i not in lose]),sorted([i for i in lose if lose[i]==1])]