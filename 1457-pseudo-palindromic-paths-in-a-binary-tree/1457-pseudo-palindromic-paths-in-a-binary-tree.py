# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def solve(root,seen):
            if not root:return 0
            
            if root.val in seen:seen.remove(root.val)
            else:seen.add(root.val)
                
            if not root.left and not root.right:
                if len(seen)<2:return 1
                return 0
            return solve(root.left,seen.copy())+solve(root.right,seen.copy())
        return solve(root,set())