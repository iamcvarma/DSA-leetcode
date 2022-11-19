# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def solve(head1,head2,carry):
            if not (head1 or head2 or carry):return None
            val1,val2,next1,next2 = 0,0,None,None
            if head1:
                val1 = head1.val
                next1 = head1.next
            if head2:
                val2 = head2.val
                next2 = head2.next
            
            curr = val1+val2+carry
            carry = curr//10
            curr = curr%10
            
            return ListNode(curr,solve(next1,next2,carry))
        return solve(l1,l2,0)
            