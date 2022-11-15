# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHeight(self,root,left):
        count=0
        while root:
            count+=1
            root = root.left if left else root.right
        return count
    
    
    def countNodes(self, root,left=None,right=None) -> int:
        if not root:return 0
        if not left:left = self.findHeight(root,True)
        if not right:right = self.findHeight(root,False)
        
        if left==right:
            return 2**(left)-1
        return self.countNodes(root.left,left-1,None)+self.countNodes(root.right,None,right-1)+1
            