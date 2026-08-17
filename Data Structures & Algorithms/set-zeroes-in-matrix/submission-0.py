class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix),len(matrix[0])
        rowZero = False

      #1st iteration to mark the rows and cols containing zero value
        for r in range(rows):
            for  c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0#it just means col c need to be zeroed later 
                    if r > 0:
                        matrix[r][0] = 0#row r need to be zeroed later 
                    else:
                        rowZero = True#first row  needs to be zeroed

        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0