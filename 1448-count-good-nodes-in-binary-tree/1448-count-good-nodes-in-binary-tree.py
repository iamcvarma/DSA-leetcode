# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count=0
    def goodNodes(self, root: TreeNode,ma=-inf) -> int:
        if not root:return
        if root.val>=ma:
            self.count+=1
        ma=max(ma,root.val)
        self.goodNodes(root.left,ma)
        self.goodNodes(root.right,ma)
        return self.count