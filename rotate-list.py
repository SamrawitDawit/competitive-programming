class ListNode:
     def __init__(self, val=0, next=None, prev =None):
         self.val = val
         self.next = next
         self.prev = prev
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        head = self.doubly_linked_list(head)
        curr = head
        count = 0
        length = 0
        while curr.next:
            curr = curr.next
            length += 1
        tail = curr
        length += 1
        k %= length
        while count != k:
            temp = tail.prev 
            tail.prev.next = None
            tail.next = head
            head = tail
            tail = temp
            count += 1
        return head
    def doubly_linked_list(self, head):
        if not head:
            return
        curr = head
        prev = None
        while curr:
            curr.prev = prev
            prev = curr 
            curr = curr.next
        return head
