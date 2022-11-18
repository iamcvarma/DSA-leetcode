# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def build(head,tail):
            if head==tail or head.next==tail:
                return head
            tail.next = build(head.next,tail.next)
            head.next=tail
            return head
                
        s=f=head
        while f and f.next:
            s=s.next
            f = f.next.next
        pre=None
        while s:
            temp = s.next
            s.next = pre
            pre = s
            s=temp
        return build(head,pre)