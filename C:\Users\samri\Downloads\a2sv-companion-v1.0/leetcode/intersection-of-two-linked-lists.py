# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ourSet = set()
        curr1 = headA
        curr2 = headB
        while curr1 and curr2:
            if curr1 in ourSet:
                return curr1
            ourSet.add(curr1)
            if curr2 in ourSet:
                return curr2 
            ourSet.add(curr2)
            curr1 = curr1.next 
            curr2 = curr2.next 
        while curr1:
            if curr1 in ourSet:
                return curr1
            curr1 = curr1.next
        while curr2:
            if curr2 in ourSet:
                return curr2
            curr2 = curr2.next
        return None