class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            new = []
            for x,y in groupby(s):
                new.append(str(len(list(y))))
                new.append(x)
            s = "".join(new)
        return s