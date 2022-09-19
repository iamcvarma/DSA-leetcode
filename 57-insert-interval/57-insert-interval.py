class Solution:
    def insert(self, arr: List[List[int]], newI: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(arr)):
            if newI[1]<arr[i][0]:
                res.append(newI)
                res.extend(arr[i:])
                return res
                
            elif arr[i][1]<newI[0]:
                res.append(arr[i])
            else:
                newI = [min(arr[i][0],newI[0]),max(arr[i][1],newI[1])]
                
        res.append(newI)
        return res