class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(' : ')', '{' : '}', '[' : ']'}
        stack = Stack()
        if len(s) == 0:
            return True
        if len(s)%2 != 0:
            return False
        for i in s:
            if i in dic.keys():
                stack.push(i)
            elif stack.size()!= 0 and dic.get(stack.peek()) == i:
                stack.pop()
            else:
                return False
        if stack.size() != 0:
          return False
        return True
