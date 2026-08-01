class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                stack.append(-stack.pop()+stack.pop())
            elif token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                if b/a>=0 or b%a==0:
                    stack.append(b//a)
                else:
                    stack.append(b//a+1)
            else:
                stack.append(int(token))
        return stack[0]