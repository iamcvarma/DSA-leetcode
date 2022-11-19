# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            pre = None
            while head:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            return pre
        
        def addLL(head1,head2,carry):
            if not (head1 or head2 or carry):return None
            v1,v2 = 0,0
            n1,n2 = None,None
            if head1:
                v1 = head1.val
                n1 = head1.next
            if head2:
                v2 = head2.val
                n2 = head2.next
            
            return ListNode((v1+v2+carry)%10,addLL(n1,n2,(v1+v2+carry)//10))
            
            
        return reverse(addLL(reverse(l1),reverse(l2),0))
            