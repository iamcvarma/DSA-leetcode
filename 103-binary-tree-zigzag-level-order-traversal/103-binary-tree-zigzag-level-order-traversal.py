# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        res=[]
        curr=[root]
        di = 1
        while curr:
            new = []
            for node in curr:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            res.append([r.val for r in curr][::di])
            di=-di
            curr=new
        return res