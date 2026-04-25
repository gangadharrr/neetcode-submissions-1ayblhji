class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        z=[]
        def makeZeroes(row_index,column_index):
            for i in range(len(matrix[row_index])):
                matrix[row_index][i] = 0
            for i in range(len(matrix)):
                matrix[i][column_index] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    z.append((i,j))
        while z:
            row_index,column_index = z.pop(0)
            makeZeroes(row_index,column_index)

        