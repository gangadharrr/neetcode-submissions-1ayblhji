class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={'{':'}','[':']','(':')'}
        for i in s:
            if stack and d.get(stack[-1], None)==i:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0