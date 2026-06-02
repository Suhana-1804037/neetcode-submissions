class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []
        curr = []
        def solve(openN, closeN):
            if openN==closeN==n:
                answer.append("".join(curr))
                return

            if openN<n:
                curr.append("(")
                solve(openN+1, closeN)
                curr.pop()
            if openN>closeN:
                curr.append(")")
                solve(openN, closeN+1)
                curr.pop()
        solve(0, 0)
        
        return answer