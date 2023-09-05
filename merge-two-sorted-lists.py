class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None :
            return list2
        elif list2 == None:
            return list1
        if list1.val < list2.val:
            curr = list1
            list1 = list1.next
        else:
            curr = list2
            list2 = list2.next
        head = curr
        while list1 != None and list2 != None:
            if list1.val<list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        if list1 == None:
            curr.next = list2
        elif list2 == None:
            curr.next = list1
        return head
