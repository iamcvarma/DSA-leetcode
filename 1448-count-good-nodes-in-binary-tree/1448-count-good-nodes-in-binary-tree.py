# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode,ma=-inf) -> int:
        if not root:return 0
        if root.val>=ma:
            count=1
            ma=root.val
        else:count=0
        return count+self.goodNodes(root.left,ma)+self.goodNodes(root.right,ma)