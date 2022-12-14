# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hmap=defaultdict(list)
        mi,ma=inf,-inf
        def tra(root,i,j):
            nonlocal mi,ma
            if not root:return
            mi=min(mi,j)
            ma=max(ma,j)
            hmap[j].append((i,root.val))
            tra(root.left,i+1,j-1)
            tra(root.right,i+1,j+1)
        tra(root,0,0)
        res=[]
        for i in range(mi,ma+1):
            res.append([y for x,y in sorted(hmap[i])])
        return res