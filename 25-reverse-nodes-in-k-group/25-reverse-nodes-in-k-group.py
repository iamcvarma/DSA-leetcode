# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start,end):
            pre = None
            while pre!=end:
                temp =start.next
                start.next = pre
                pre = start
                start = temp
        if not head:return head
        st=end=head
        for _ in range(k-1):
            if not end:break
            end=end.next
        if not end:return head
        temp = end.next
        reverse(st,end)
        st.next = self.reverseKGroup(temp,k)
        return end
            