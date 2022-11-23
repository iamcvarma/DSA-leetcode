class ListNode:
    def __init__(self,val=-1,N=None,P=None):
        self.val=val
        self.next = N
        self.pre = P
        
class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, i: int) -> int:
        curr = self.head.next
        while i and curr!=self.tail:
            curr ,i= curr.next,i-1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val,self.head.next,self.head)
        self.head.next = newNode
        newNode.pre = self.head
        newNode.next.pre = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val,self.tail,self.tail.pre)
        self.tail.pre = newNode
        newNode.pre.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
            if not curr:return
        newNode = ListNode(val,curr,curr.pre)
        curr.pre = newNode
        newNode.pre.next= newNode
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        if curr==self.tail:return
        for _ in range(index):
            curr = curr.next
            if curr==self.tail:return
        curr.next.pre = curr.pre
        curr.pre.next = curr.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)