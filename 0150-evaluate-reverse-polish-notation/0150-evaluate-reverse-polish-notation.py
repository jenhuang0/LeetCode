class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in '+-*/':
                stack.append(int(tokens[i]))
            else:
                op = tokens[i]
                num2 = stack.pop()
                num1 = stack.pop()

                if op =='+':
                    stack.append(num1 + num2)
                elif op == '-':
                    stack.append(num1 - num2)
                elif op == '*':
                    stack.append(num1 * num2)
                elif op == '/':
                    stack.append(int(num1 / num2))
        return stack[-1]