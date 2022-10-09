# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def solve(root):
            nonlocal res
            if not root or res:return
            solve(root.left)
            if k-root.val in d:
                res=True
                return
            d.add(root.val)
            solve(root.right)
        d=set()
        res=False
        solve(root)
        return res
        