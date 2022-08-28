class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        null_flag=False
        q=deque([root])
        
        while q:
            curr=q.popleft()
            if not curr:
                null_flag=True
            else:
                if null_flag:return False
                q.append(curr.left)
                q.append(curr.right)
        return True