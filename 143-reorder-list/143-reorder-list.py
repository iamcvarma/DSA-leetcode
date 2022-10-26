# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:return head
        
        def build(h1,h2):
            if not h1 or not h2:
                return h1
            h2.next = build(h1.next,h2.next)
            h1.next = h2
            return h1
        
        
        def reverse(head):
            pre=None
            while head:
                head.next,head,pre = pre,head.next,head
            return pre
        
        
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        end = reverse(slow.next)
        slow.next = None
        
        build(head,end)
        