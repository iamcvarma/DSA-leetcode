"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        res=[]
        q=[root]
        while q:
            new=[]
            for node in q:
                for ch in node.children:
                    new.append(ch)
            res.append([r.val for r in q])
            q=new
        return res