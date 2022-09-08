# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative
        st,res,curr=[],[],root
        while st or curr:
            while curr:
                st.append(curr)
                curr=curr.left
            root=st.pop()
            res.append(root.val)
            curr=root.right
        return res