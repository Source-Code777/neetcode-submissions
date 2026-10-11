class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        for ch in s:
            if ch=='(' or ch=='{' or ch=='[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                e=stack.pop()
                if (ch=='}' and e!='{') or (ch==']' and e!='[') or (ch==')' and e!='('):
                    return False

        return len(stack)==0
        