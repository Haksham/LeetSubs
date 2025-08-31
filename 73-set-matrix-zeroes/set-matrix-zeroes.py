from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        rows = set()
        cols = set()
        
        # Pass 1: record which rows and cols need zeroing
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Pass 2: update rows
        for i in rows:
            for j in range(m):
                matrix[i][j] = 0
        
        # Pass 3: update cols
        for j in cols:
            for i in range(n):
                matrix[i][j] = 0
