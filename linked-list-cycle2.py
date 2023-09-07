class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = {}
        while head != None:
            if id(head) in dic:
                dic = None
                return head
            dic[id(head)] = 1
            head = head.next
        dic = None
        return None
