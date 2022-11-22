class Solution:
    def largestVariance(self, s: str) -> int:
        freq = Counter(s)
        ma=0
        for c1 in freq:
            for c2 in freq:
                if c1==c2:continue
                a=0
                b=0
                remC1 = freq[c1]
                for c in s:
                    if c==c1:
                        a+=1
                        remC1-=1
                    elif c==c2:
                        b+=1
                    else:continue
                    if remC1>0 and b<a:
                        a=0
                        b=0
                    if a and b and b-a>ma:
                        ma=b-a
        return ma
                