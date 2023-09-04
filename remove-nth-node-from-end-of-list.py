class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        k = count - n
        curr = head
        if k == 0:
            temp = head.next
            head.next = None
            return temp
        count = 1
        while count < k:
           curr = curr.next
           count += 1
        curr.next = curr.next.next
        return head
