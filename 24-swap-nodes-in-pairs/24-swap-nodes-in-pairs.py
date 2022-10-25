# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head
        tail = head.next
        temp = tail.next
        tail.next = head
        head.next = self.swapPairs(temp)
        return tail