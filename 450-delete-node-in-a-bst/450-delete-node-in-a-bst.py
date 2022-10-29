# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node,child):
            if not node:return child
            node.right = delete(node.right,child)
            return node
        def traverse(root,key):
            if not root:return None
            if root.val<key:
                root.right = traverse(root.right,key)
            elif root.val>key:
                root.left = traverse(root.left,key)
            else:return delete(root.left,root.right)
            return root
        
        return traverse(root,key)