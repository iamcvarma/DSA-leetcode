class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d={}
        for n in arr:
            if 2*n in d or n/2 in d:
                return True
            d[n]=1
        
        return False