class LeftIter:
    def __init__(self,root):
        self.st=[]
        self.add(root)
    
    def add(self,root):
        while root:
            self.st.append(root)
            root=root.left
    def nxt(self):
        res=self.st.pop()
        self.add(res.right)
        return res.val
    
class RightIter:
    def __init__(self,root):
        self.st=[]
        self.add(root)
    
    def add(self,root):
        while root:
            self.st.append(root)
            root=root.right
    def nxt(self):
        res=self.st.pop()
        self.add(res.left)
        return res.val


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lt =LeftIter(root)
        rt = RightIter(root)
        left,right = lt.nxt(),rt.nxt()
        while left<right:
            if left+right==k:return True
            elif left+right<k:
                left=lt.nxt()
            else:
                right = rt.nxt()
        return False