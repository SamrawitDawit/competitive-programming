# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        lst = []
        while curr != None:
            lst.append(curr.val)
            curr = curr.next
        lst.sort()
        curr = head
        for num in lst:
            curr.val = num
            curr = curr.next
        return head
