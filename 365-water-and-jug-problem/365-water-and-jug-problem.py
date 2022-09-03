class Solution:
    def canMeasureWater(self,a: int, b: int, z: int) -> bool:
        if a+b<z:return False
        if a<b:a,b=b,a
        arr=[a,b,-a]
        seen=set([0])
        q=deque([0])
        while q:
            curr=q.pop()
            for n in arr:
                val=n+curr
                if val==z:return True
                if 0<=val<=a+b and val not in seen:
                    seen.add(val)
                    q.append(val)
        return False