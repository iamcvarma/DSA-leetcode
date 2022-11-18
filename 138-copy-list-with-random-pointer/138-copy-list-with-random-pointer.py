"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = ptr = Node(-1)
        hmap={None:None}
        while head:
            ptr.next = Node(head.val,None,head.random)
            ptr = ptr.next
            hmap[head] = ptr
            head = head.next
        
        ptr = dummy.next
        while ptr:
            ptr.random = hmap[ptr.random]
            ptr = ptr.next
        return dummy.next