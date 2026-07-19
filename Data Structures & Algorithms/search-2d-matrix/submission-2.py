class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       m = len(matrix) # no of rows
       n = len(matrix[0]) # no of columns

       l,r = 0,m * n -1

       while l<=r:
         mid = l + (r-l)//2

         row = mid//n
         col = mid % n
         
         if target > matrix[row][col]:
            l = mid + 1
         elif target < matrix[row][col]:
            r = mid - 1
         else:
            return True
       return False