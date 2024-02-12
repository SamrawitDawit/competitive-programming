class Node:
    def __init__(self, node, nxt=None):
        self.val = node
        self.next = nxt
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.dummy = Node('Empty')
        self.dummy.next = self.head
    def get(self, index: int) -> int:
        curr_index = 0
        curr_node = self.head
        while curr_index != index:
            curr_node = curr_node.next if curr_node else None
            curr_index += 1
        return curr_node.val if curr_node else -1
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = new_node
        self.head = self.dummy.next

        # curr = self.head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next if curr else None
        # print('end')
    def addAtIndex(self, index: int, val: int,) -> None:
        new_node = Node(val)
        curr_index = -1
        curr = self.dummy
        while curr and curr_index + 1 != index:
            curr = curr.next
            curr_index += 1
        if curr: 
            new_node.next = curr.next
            curr.next = new_node
        self.head = self.dummy.next
        
        # curr = self.head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next if curr else None
        # print('end')
    def deleteAtIndex(self, index: int) -> None:
        curr_index = -1
        curr = self.dummy
        while curr_index + 1 != index:
            if not curr:
                return 
            curr = curr.next 
            curr_index += 1
        if curr:
            if curr.next:
                curr.next = curr.next.next 
        self.head = self.dummy.next
        
        # curr = self.head
        # while curr:
        #     print(curr.val)
        #     curr = curr.next if curr else None
        # print('end')
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)