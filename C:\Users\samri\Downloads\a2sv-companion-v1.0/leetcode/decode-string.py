class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                letter, num = '', ''
                while stack[-1] != '[':
                    letter = stack.pop() + letter
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(letter*int(num))
        return ''.join(stack)
            