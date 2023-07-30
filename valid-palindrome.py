class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for i in s:
            i = i.lower()
            if i.isalnum():
                string += i
        while len(string) != 0:
            if string[0] != string[-1]:
                return False
            string = string[1:-1]
        return True
