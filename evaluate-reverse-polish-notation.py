class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if num == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif num == "-":
                int2, int1 = stack.pop(), stack.pop()
                stack.append(int1-int2)
            elif num == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif num == "/":
                int2, int1 = stack.pop(), stack.pop()
                stack.append(int(int1/int2))
            else:
                stack.append(int(num))
        return stack[0]
