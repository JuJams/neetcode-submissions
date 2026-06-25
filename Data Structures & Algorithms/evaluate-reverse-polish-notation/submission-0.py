class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
        # print(stack) 
            else:
                b = stack.pop()
                a = stack.pop()
                print(b)
                print(a)
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        #print(stack)
        return stack[-1]



            
        