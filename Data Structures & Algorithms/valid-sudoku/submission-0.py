class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unseen= set()
        for i in range(9):
            seen= set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                
                if board[i][j] in seen:
                    return False
                
                seen.add(board[i][j])
        
        for i in range(9):
            seen= set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                
                if board[j][i] in seen:
                    return False
                
                seen.add(board[j][i])
        
        for row in range(0,9,3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(row, row+3, 1):
                    for j in range(col, col+3, 1):
                        if board[i][j]=='.':
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])

        return True


