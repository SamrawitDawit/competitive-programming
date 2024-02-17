class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        left = 0
        right = len(palindrome)-1
        output = ''
        if len(palindrome) == 1:
            return output
        while left < right and palindrome[left] == 'a':
            left += 1
            right -= 1
        if left < right:
            output = palindrome[:left] + 'a' + palindrome[left+1:]
        else:
            output = palindrome[:-1] + 'b'
        return output