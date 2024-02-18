class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        for elem in tokens:
            if elem not in operations:
                stack.append(int(elem))
            else:
                num1= stack.pop()
                num2= stack.pop()
                if elem == '+':
                    stack.append(num1+num2)
                elif elem == '-':
                    stack.append(num2-num1)
                elif elem == '*':
                    stack.append(num2*num1)
                else:
                    stack.append(int(num2/num1))
        return stack[0]

        