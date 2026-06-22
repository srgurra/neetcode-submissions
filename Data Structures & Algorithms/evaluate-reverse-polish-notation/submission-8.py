class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators= set(['+', '*', '-', '/'])
        stack=[]
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                a=int(stack.pop())
                b=int(stack.pop())
                if token=='+':
                    stack.append(a+b)
                elif token== '-':
                    stack.append(b-a)
                elif token =='*':
                    stack.append(b*a)
                else:
                    if b/a<0:
                        stack.append(math.ceil(b/a))
                    else:
                        stack.append(math.floor(b/a))

            print(stack)
        return int(stack[0])      