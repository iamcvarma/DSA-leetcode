# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:return None
        s=f=head
        while f and f.next:
            pre,s,f=s,s.next,f.next.next
        pre.next=s.next
        return head