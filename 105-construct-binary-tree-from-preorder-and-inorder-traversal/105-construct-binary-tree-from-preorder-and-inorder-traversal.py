# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:return None
        root = preorder.pop(0)
        mid = inorder.index(root)
        return TreeNode(root,self.buildTree(preorder,inorder[:mid]),self.buildTree(preorder,inorder[mid+1:]))