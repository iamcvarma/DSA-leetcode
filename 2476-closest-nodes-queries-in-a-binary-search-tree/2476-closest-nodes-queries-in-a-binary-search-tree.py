# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr=[]
        res=[]
        def tra(root,arr):
            if not root:return 
            tra(root.left,arr)
            arr.append(root.val)
            tra(root.right,arr)
            return
        tra(root,arr)
        
        for q in queries:
            i = bisect.bisect_left(arr,q)
            low = arr[i-1] if i else -1 
            high = arr[i] if i<len(arr) else -1
            res.append([low,high] if high!=q else [q,q])
        return res