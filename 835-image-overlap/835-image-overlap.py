class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        hmap,n=defaultdict(int),len(img1)
        arr=[]
        for i in range(n):
            for j in range(n):
                if img2[i][j]:
                    arr.append((i,j))
        
        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    for x,y in arr:
                        hmap[(x-i,y-j)]+=1
        return max(hmap.values(),default=0)