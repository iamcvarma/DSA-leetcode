# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=[root]
        res=[]
        while q:
            new=[]
            avr=0
            for n in q:
                avr+=n.val
                if n.left:
                    new.append(n.left)
                if n.right:
                    new.append(n.right)
            res.append(avr/len(q))
            q=new
        return res