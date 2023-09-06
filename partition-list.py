class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head and head.val >= x:
            greater = head
            curr = head
            prev = None
        else:
            curr = head
            while curr:
                prev = curr
                curr = curr.next
                if curr and curr.val >= x:
                    greater = curr 
                    break
        while curr:
            prev2 = curr
            curr = curr.next
            if curr and curr.val < x:
                prev2.next = curr.next
                curr.next = greater
                if prev:
                    prev.next = curr
                else:
                    head = curr
                prev = curr
        return head
