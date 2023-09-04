class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        count = 0
        curr = head
        prev = curr
        nxt = curr.next
        while curr:
            if count%2 != 0 and curr.next:
                temp = curr.next
                curr.next = curr.next.next
                prev.next = temp
                temp.next = nxt
                prev = temp
            else:
                curr = curr.next
            count += 1
        return head
