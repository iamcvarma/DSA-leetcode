"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.hmap={}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:return node
        if node.val in self.hmap:return self.hmap[node.val]
        curr = Node(node.val)
        self.hmap[curr.val] =curr 
        curr.neighbors = [self.cloneGraph(nei) for nei in node.neighbors]
        return curr