class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        while curr.next:
            prev = curr
            curr.val = curr.next.val
            curr = curr.next
        prev.next = None
