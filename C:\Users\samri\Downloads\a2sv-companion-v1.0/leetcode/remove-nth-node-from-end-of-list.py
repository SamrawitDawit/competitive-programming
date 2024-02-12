# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        forward_pointer = head
        curr_indx = 0
        while curr_indx != n:
            forward_pointer = forward_pointer.next
            curr_indx += 1
        backward_pointer = head
        if forward_pointer == None:
            return backward_pointer.next
        while forward_pointer.next:
            forward_pointer = forward_pointer.next
            backward_pointer = backward_pointer.next
        backward_pointer.next = backward_pointer.next.next if backward_pointer.next else None
        return head
