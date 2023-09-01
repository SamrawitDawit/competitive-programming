class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
        count2 = 0
        curr = head
        while count2 != (count//2):
            curr = curr.next
            count2 += 1
        return curr
