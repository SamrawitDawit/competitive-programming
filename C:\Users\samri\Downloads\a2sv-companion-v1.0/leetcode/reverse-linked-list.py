# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.old_head = head 
        if head == None or head.next == None:
            return head
        return self.reverse(head)
    def reverse(self,head):
        if head.next == None:
            self.new_head = head
            return self.new_head
        temp = self.reverse(head.next)
        temp.next = head
        if self.old_head == head:
            head.next = None
            return self.new_head
        return head
