# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return 1
        left,right = self.isBalanced(root.left),self.isBalanced(root.right)
        if not left or not right:return False
        if abs(left-right)>1:return False
        return max(left,right)+1
    