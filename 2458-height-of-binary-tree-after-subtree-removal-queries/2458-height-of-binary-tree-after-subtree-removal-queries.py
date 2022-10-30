# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def calcHeight(node):
            if not node:
                return 0
            height[node.val] = max(calcHeight(node.left),calcHeight(node.right))+1
            return height[node.val]
        height={}
        calcHeight(root)
        res={}
        def dfs(root,depth,ma):
            if not root:return
            res[root.val] = ma
            dfs(root.left,depth+1,max(ma,depth+(height[root.right.val] if root.right else 0)))
            dfs(root.right,depth+1,max(ma,depth+(height[root.left.val] if root.left else 0)))
            return 
        dfs(root,0,0)
        return [res[i] for i in queries]