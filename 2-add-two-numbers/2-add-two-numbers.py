# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def solve(num1,num2,carry):
            if not num1 and not num2:
                if carry: return ListNode(carry)
                return None
            ans = (num1.val if num1 else 0) + (num2.val if num2 else 0 )+carry
            node = ListNode(ans%10)
            node.next = solve(num1.next if num1 else num1,num2.next if num2 else num2,ans//10)
            return node
        return solve(l1,l2,0)