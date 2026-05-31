class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        curr = ""
        n, m = len(board), len(board[0])
        def solve(i,r,c):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=n or c>=m or word[i]!=board[r][c] or board[r][c]=='#':
                return False
            board[r][c]='#'

            ans = solve(i+1, r+1, c) or solve(i+1, r-1, c) or solve(i+1, r, c+1) or solve(i+1, r, c-1)
            board[r][c] =word[i]
            return ans

        for i in range(n):
            for j in range(m):
                if solve(0,i, j):
                    return True
        return False