# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def solve(node,curr,ans,res):
            if not node:return
            if curr==node.val and not node.left and not node.right:
                res.append(ans[:]+[node.val])
                return
            ans.append(node.val)
            curr-=node.val
            solve(node.left,curr,ans,res)
            solve(node.right,curr,ans,res)
            ans.pop()
            
        res=[]
        solve(root,targetSum,[],res)
        return res