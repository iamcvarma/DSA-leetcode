class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q=deque([start])
        seen=set()
        while q:
            i=q.popleft()
            if not (-1<i<len(arr)) or i in seen:continue
            seen.add(i)
            num=arr[i]
            if num==0:return True
            q.append(i-num)
            q.append(i+num)
        return False