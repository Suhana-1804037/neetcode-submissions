class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p=""
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                p = stack[-1]
                if ((p=="(" and c==")") or (p=="{" and c=="}") or (p=="[" and c=="]")):
                    stack.pop()
                else:
                    return False
        return len(stack)==0