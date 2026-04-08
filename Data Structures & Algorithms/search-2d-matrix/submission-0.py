class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left, row_right = 0, len(matrix[0])-1
        col_left, col_right = 0, len(matrix)-1
        while col_left < col_right:
            val = (col_left + col_right)//2
            if matrix[val][0] == target:
                return True
            elif matrix[val][0] < target:
                if matrix[val+1][0] > target:
                    col_left = val
                    break
                else:
                    col_left = val + 1
            else:
                if matrix[val-1][0] < target:
                    col_right = val - 1
                    col_left = val - 1
                    break
                else:
                    col_right = val
        while row_left <= row_right:
            val = (row_left + row_right)//2
            if matrix[col_left][val] == target:
                return True
            elif matrix[col_left][val] < target:
                row_left = val+1
            else:
                row_right = val-1
        return False
        