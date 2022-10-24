# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = p= ListNode(0)
        while curr:
            if curr.next and curr.val==curr.next.val:
                temp = curr.val
                while curr and curr.val==temp:
                    curr = curr.next
            else:
                p.next = ListNode(curr.val)
                p = p.next
                curr=curr.next
        return dummy.next