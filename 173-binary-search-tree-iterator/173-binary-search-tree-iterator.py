# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st=[]
        self.insertLeft(root)

    def next(self) -> int:
        curr = self.st.pop()
        self.insertLeft(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        return self.st
    
    def insertLeft(self,root):
        while root:
            self.st.append(root)
            root=root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()