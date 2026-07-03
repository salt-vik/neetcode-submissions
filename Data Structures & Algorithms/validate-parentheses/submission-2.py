class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s :
            if stack and i==')' and stack[-1]=='(' :
                stack.pop()
            elif stack and i==']' and stack[-1]=='[' :
                stack.pop()
            elif stack and i=='}' and stack[-1]=='{' :
                stack.pop()
            elif i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                return False
        if not stack:
            return True
        else:
            return False
        