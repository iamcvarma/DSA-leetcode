# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def solve(root,curr,ans,res):
            if not root:return
            ans.append(root.val)
            curr-=root.val
            if not(root.left or root.right or curr):
                res.append(ans[::])
            
            solve(root.left,curr,ans,res)
            solve(root.right,curr,ans,res)
            ans.pop()
            return
        res=[]
        solve(root,targetSum,[],res)
        return res