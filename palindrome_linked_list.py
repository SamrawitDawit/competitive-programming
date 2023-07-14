# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        helper_list = []
        while head != None:
            helper_list.append(head.val)
            head = head.next
        return self.helper(helper_list)
    def helper(self, the_list):
        if len(the_list) == 1 or len(the_list) == 0:
            return True
        if the_list[0] == the_list[-1]:
            the_list.pop(0)
            the_list.pop(-1)
            return self.helper(the_list)
        return False
