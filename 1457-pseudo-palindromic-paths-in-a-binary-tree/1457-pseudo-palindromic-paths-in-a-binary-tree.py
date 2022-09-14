# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def solve(root,mask):
            if not root:return 0
            mask^=1<<root.val
            if not root.left and not root.right:
                if mask==0 or mask&mask-1==0:
                    return 1
                return 0
            return solve(root.left,mask)+solve(root.right,mask)
        
        
        return solve(root,0)