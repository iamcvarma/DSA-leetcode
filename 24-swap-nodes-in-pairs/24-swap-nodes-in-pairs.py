# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0,head)
        while pre and pre.next and pre.next.next:
            curr = pre.next
            nxt  = curr.next
            temp = nxt.next
            nxt.next = curr
            pre.next = nxt
            curr.next = temp
            pre = curr
        return dummy.next