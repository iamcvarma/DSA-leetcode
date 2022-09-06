# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def tra(root):
            if not root:return False
            left=tra(root.left)
            right=tra(root.right)
            if not left:root.left=None
            if not right:root.right=None
            return root.val==1 or left or right
        if not tra(root):return None
        return root