class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        box = [[{} for j in range(3)] for i in range(3)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.': 
                    continue
                if row[i].get(board[i][j], False):
                    return False
                else:
                    row[i][board[i][j]] = True
                if col[j].get(board[i][j], False):
                    return False
                else:
                    col[j][board[i][j]] = True
                if box[i//3][j//3].get(board[i][j], False):
                    return False
                else:
                    box[i//3][j//3][board[i][j]] = True
        return True
        