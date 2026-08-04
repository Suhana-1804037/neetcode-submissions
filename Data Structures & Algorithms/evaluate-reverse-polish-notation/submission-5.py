class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for st in tokens:
            val = 0
            if st in "+-*/":
                val1 = stack[-1]
                stack.pop()
                val2 = stack[-1]
                stack.pop()
                
                if st=="+":
                    val = val1+val2
                elif st=="-":
                    val = val2-val1
                elif st=="*":
                    val = val2*val1
                elif st=="/":
                    val = int(val2 / val1)
                
            else:
                val = int(st)
            stack.append(val)

        return stack[-1]

