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
        if not head:return head
        root = head
        while head:
            newNode = Node(head.val,head.next,head.random)
            head.next = newNode
            head = newNode.next
        dummy = ptr =Node(-1)
        curr = root.next
        while curr:
            ptr.next = curr
            if curr.random:   
                curr.random = curr.random.next
            ptr = ptr.next
            curr.next = curr.next.next if curr.next else None
            curr = curr.next
        return dummy.next