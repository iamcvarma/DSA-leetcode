class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(curr):
            if curr in seen:return 0
            seen.add(curr)
            return 1+sum((dfs(j) for j in rooms[curr]),0)
        seen=set()
        return len(rooms)==dfs(0)