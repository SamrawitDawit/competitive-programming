class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr and curr.next:
            if curr.val == curr.next.val:
                if prev:
                    left = prev
                    while curr and curr.val == left.next.val:
                        curr = curr.next
                    left.next = curr
                else:
                    left = curr
                    while curr and curr.val == left.val:
                        curr = curr.next
                    head = curr
            else:
                prev = curr
                curr = curr.next
        return head 
