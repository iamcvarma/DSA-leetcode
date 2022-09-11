class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #morris Traversal
        res=[]
        while root:
            if root.left==None:
                res.append(root.val)
                root = root.right
            else:
                ptr = root.left
                while ptr.right and ptr.right!=root:
                    ptr = ptr.right
                if not ptr.right:
                    ptr.right = root
                    root = root.left
                else:
                    ptr.right = None
                    res.append(root.val)
                    root = root.right
        return res