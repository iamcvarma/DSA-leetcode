class ListNode:
    def __init__(self,val = 0,nxt = None,pre=None):
        self.val = val
        self.nxt = nxt
        self.pre = pre

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        node = self.goto(index)
        return node.val if node else -1
        
        
    def goto(self,index):
        if index>=self.length:return None
        curr = self.head
        for _ in range(index):
            curr = curr.nxt
        return curr
    
    
    def addAtHead(self, val: int) -> None:
        node = ListNode(val,self.head)
        if self.head:
            self.head.pre = node
        self.head = node
        self.length+=1
        # self.view()
        return None
    
    
    
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        curr = self.head
        while curr.nxt:curr = curr.nxt
        node = ListNode(val,None,curr)
        curr.nxt = node
        self.length+=1
        # self.view()
        return None
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index==self.length:
            self.addAtTail(val)
            return
        if index==0:
            self.addAtHead(val)
            return
        node = self.goto(index)
        if not node:return
        new_node = ListNode(val,node,node.pre)
        if node.pre: 
            node.pre.nxt = new_node
        node.pre = new_node
        self.length+=1
        # self.view()
    
    
    
    def deleteAtIndex(self, index: int) -> None:
        node = self.goto(index)
        if not node:return
        if node.pre:
            node.pre.nxt = node.nxt
        if node.nxt:
            node.nxt.pre = node.pre
        if node==self.head:self.head = node.nxt
        node.pre=node.nxt = None
        self.length-=1
        # self.view()
        return
    
    def view(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur=cur.nxt
        print('end')


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)