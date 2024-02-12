# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1
        count = 0
        curr = head
        while count != (length//2):
            curr = curr.next
            count += 1
        return curr

        