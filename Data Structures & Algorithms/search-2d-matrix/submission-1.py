class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = dict()

        for i in range(len(matrix)):
            rows[i] = matrix[i]
        
        for k in range(len(matrix)):
            if target in rows.get(k):
                return True
        
        return False