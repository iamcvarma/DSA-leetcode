class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(curr):
            if curr in seen:return
            seen.add(curr)
            for nei in rooms[curr]:
                dfs(nei)
        seen=set()
        dfs(0)
        return len(seen)==len(rooms)