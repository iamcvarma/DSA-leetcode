"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        st=[]
        node=head
        while node or st:
            if node.child:
                if node.next:st.append(node.next)
                node.next=node.child
                node.child=None
                node.next.prev=node
            elif not node.next and st:
                node.next=st.pop()
                node.next.prev=node
            node=node.next
        return head