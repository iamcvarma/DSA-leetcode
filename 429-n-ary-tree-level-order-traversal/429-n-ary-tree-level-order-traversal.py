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
            res.append([])
            for node in q:
                res[-1].append(node.val)
                for ch in node.children:
                    new.append(ch)
            
            q=new
        return res