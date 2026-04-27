class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(board, row, col, word, record, pointer):
            if len(word)-1 == pointer and board[row][col] == word[pointer]:
                return True
            elif board[row][col] == word[pointer]:
                record[(row,col)] = False
                pointer+=1
                truthTable = []
                if row - 1 >=0 and record.get((row-1, col), True):
                    truthTable.append(check(board, row-1,col,word, record.copy(), pointer))
                if row + 1 < len(board) and record.get((row+1, col), True):
                    truthTable.append(check(board, row+1,col,word, record.copy(), pointer))
                if col - 1 >=0 and record.get((row, col-1), True):
                    truthTable.append(check(board, row,col-1,word, record.copy(), pointer))
                if col + 1 < len(board[row]) and record.get((row, col+1),True):
                    truthTable.append(check(board, row,col+1,word, record.copy(), pointer))
                return len(truthTable) > 0  and any(truthTable)
            else:
                return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    checked_val = check(board, i, j, word, {}, 0)
                    if checked_val:
                        return True

        return False