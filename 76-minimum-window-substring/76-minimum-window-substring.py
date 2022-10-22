class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) :return ""
        i,mi,idx = 0,inf,0
        count = len(t)
        hmap = Counter(t)
        for j,ch in enumerate(s):
            if ch in hmap:
                hmap[ch]-=1
                if hmap[ch]>-1:
                    count-=1
            while not count:
                if s[i] in hmap:
                    hmap[s[i]]+=1
                    if hmap[s[i]]>0:
                        count+=1
                if (j-i+1)<mi:
                    mi = j-i+1
                    idx = i
                i+=1
        if mi==inf:return ""     
        return s[idx:idx+mi]