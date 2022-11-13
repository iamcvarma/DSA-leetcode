"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return root
        res=[]
        lvl=[root]
        while lvl:
            new = []
            for curr in lvl:
                for child in curr.children:
                    if child:
                        new.append(child)
            res.append([root.val for root in lvl])
            lvl = new
        return res