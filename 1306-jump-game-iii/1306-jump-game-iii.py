class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=deque([start])
        seen=set()
        while q:
            curr=q.pop()
            if arr[curr]==0:return True
            if curr in seen:continue
            seen.add(curr)
            if -1<curr-arr[curr]<len(arr):
                q.append(curr-arr[curr])
            if -1<curr+arr[curr]<len(arr):
                q.append(curr+arr[curr])
        return False