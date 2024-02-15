# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        count = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while count != left:
            prev = prev.next 
            count += 1
        previous = prev     
        curr = prev.next
        leftN = curr
        while count < right+1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        previous.next = prev
        leftN.next = curr
        return dummy.next

