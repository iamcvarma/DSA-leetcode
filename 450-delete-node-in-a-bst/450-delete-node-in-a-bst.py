# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node):
            if not node.left or not node.right:
                return node.left or node.right
            temp = node.left
            while temp.right:
                temp=temp.right
            temp.right = node.right
            return node.left
        def traverse(root,key):
            if not root:return None
            if root.val<key:
                root.right = traverse(root.right,key)
            elif root.val>key:
                root.left = traverse(root.left,key)
            else:return delete(root)
            return root
        
        return traverse(root,key)