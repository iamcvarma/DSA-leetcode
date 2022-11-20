# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findLength(head):
            count = 0
            while head:
                count+=1
                head = head.next
            return count
        if k==0 or not head:return head
        n = findLength(head)
        k = k%n
        if not k:return head
        s=f=head
        for _ in range(k):
            f = f.next
        while f.next:
            s = s.next
            f = f.next
        f.next = head
        ans = s.next
        s.next = None
        return ans