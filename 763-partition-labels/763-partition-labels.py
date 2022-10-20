class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i,c in enumerate(s):last[c] = i
            
        res = []
        pre=0
        ma = 0
        for i,c in enumerate(s):
            ma = max(ma,last[c])
            if i==ma:
                res.append(i-pre+1)
                pre=i+1
        return res