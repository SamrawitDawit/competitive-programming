class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_set = set()
        current = head
        while current != None:
            if current.next in nodes_set:
                del nodes_set
                return True
            else:
                nodes_set.add(current)
                current = current.next
        return False
