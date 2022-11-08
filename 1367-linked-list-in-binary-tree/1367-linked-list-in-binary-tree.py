# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def solve(head,root,node):
            if not node:return True
            if not root:return False
            if root.val == node.val:
                if solve(head,root.left,node.next) or solve(head,root.right,node.next):
                    return True
            if head==node:
                return solve(head,root.left,node) or solve(head,root.right,node)
            return False
        return solve(head,root,head)