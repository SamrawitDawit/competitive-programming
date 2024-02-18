# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        if k >= length:
            curr, i= head, 0
            output = [None] * k
            while curr:
                output[i] = curr
                nxt = curr.next
                curr.next = None 
                curr = nxt
                i += 1
            return output
        parts = length//k
        remainder = length%k 
        output = []
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy
        while curr:
            thisHead = dummy.next
            curr, count = dummy, 0
            while curr and count != parts:
                curr = curr.next
                count += 1
            if remainder:
                curr = curr.next
                remainder -= 1
            if curr:
                dummy.next = curr.next
                curr.next = None
                output.append(thisHead)
        return output

