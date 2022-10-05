# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def solve(root,depth,val,left):
            
            if depth==1:
                new = TreeNode(val)
                if left:
                    new.left=root
                else:new.right=root
                return new
            if not root:return None
            root.left = solve(root.left,depth-1,val,1)
            root.right=solve(root.right,depth-1,val,0)
            return root
        return solve(root,depth,val,1)