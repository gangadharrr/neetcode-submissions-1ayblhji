class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "*": lambda x,y: x*y, 
            "+": lambda x,y: x+y,
            "/": lambda x,y: int(x/y),
            "-": lambda x,y: x-y
            }
        
        for i in tokens:
            if operations.get(i, False):
                second = stack.pop()
                first = stack.pop()
                stack.append(operations[i](first, second))
            else:
                stack.append(int(i))
        return stack[-1]
        