# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        leftH,rightH=0,0
        curr = root.left
        while curr:
            leftH+=1
            curr=curr.left
        curr = root.right
        while curr:
            rightH+=1
            curr = curr.left
        
        if leftH==rightH:
            return 2**leftH+self.countNodes(root.right)
        else:
            return 2**rightH+self.countNodes(root.left)