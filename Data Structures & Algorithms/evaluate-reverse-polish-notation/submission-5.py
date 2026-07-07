class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            print(stack,i)
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:
                x=stack.pop()
                y=stack.pop()
                if i=='+':
                    stack.append(y+x)
                if i=='-':
                    stack.append(y-x)
                if i=='*':
                    stack.append(y*x)
                if i=='/':
                    stack.append(int(y/x))
        return stack[0]
        