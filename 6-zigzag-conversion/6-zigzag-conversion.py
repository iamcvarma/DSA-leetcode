class Solution:
    def convert(self, s: str, m: int) -> str:
        if m==1:return s
        i= 0
        arr = [[] for _ in range(m)]
        for c in s:
            if i==0: di = 1
            if i==m-1: di = -1
            arr[i].append(c)
            i+=di
        return "".join(["".join(a) for a in arr])