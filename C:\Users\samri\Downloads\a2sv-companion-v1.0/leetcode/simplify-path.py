class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path.split('/'):
            if char == '':
                pass
            elif char == '.':
                pass
            elif char == '..':
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(char)
        return '/'+'/'.join(stack)
