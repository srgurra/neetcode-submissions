class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=set(['+', '-', '*', '/'])
        ans=0
        for tok in tokens:
            if tok not in operators:
                stack.append(int(tok))
            else:
                if tok== '+':
                    ans= stack.pop()+ stack.pop()
                    
                elif tok== '-':
                    ans= -stack.pop()+stack.pop()
                elif tok == '*':
                    ans= stack.pop()*stack.pop()
                else:
                    num2 = stack.pop()
                    num1= stack.pop()
                    ans= int(num1/num2)
                stack.append(ans)

        return stack[-1]