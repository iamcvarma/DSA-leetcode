class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s,e = 0,len(letters)
        while s<e:
            m = s+e>>1
            if ord(letters[m])>ord(target):
                e=m
            else:
                s = m+1
        return letters[s%len(letters)]