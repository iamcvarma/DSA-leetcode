class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def bisearch(idx):
            s,e = 0,len(mat[idx])
            while s<e:
                m = s+e>>1
                if mat[idx][m]:
                    s=m+1
                else:
                    e = m
            return s
        arr = [(bisearch(i),i) for i in range(len(mat))]
        return [ar[1] for ar in sorted(arr)[:k]]