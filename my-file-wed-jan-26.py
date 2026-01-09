"""Toeplitz"""

from typing import List

def is_toeplitz(matrix: List[List[int]]) -> bool:
   n = len(matrix)
   
   for i in range(1, n):
      for j in range(1, n):
         if matrix[i][j] != matrix[i - 1][j - 1]:
            return False
         
   return True

""" optimized search """
def count_less_than(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    
    row = 0
    col = cols - 1
    count = 0
    while row < rows and col >= 0:
        if matrix[row][col] < target:
            count += col + 1 
            row += 1 
        else:
            col -= 1 
               
    return count

""" min max on diagonal """
def solution(grid):
    if not grid:
        return [None, None]
    
    rows = len(grid)
    cols = len(grid[0])
    max = min = grid[0][cols - 1]
    row = 1
    col = cols - 2
    
    while row < rows and col >= 0:
        if grid[row][col] < min:
            min = grid[row][col]
        elif grid[row][col] > max:
            max = grid[row][col]
        
        row += 1
        col -= 1
    
    return [min, max]

""" target search """
def find_row_with_target(matrix: list[list[int]], target: int) -> int | None:
    # TODO: Implement the solution here
    output = None
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    row = 0
    col = cols - 1
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return row
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    
    return output


""" reverse """
def solution(arr):
    # TODO: Implement in-place array reverse.
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        right -= 1
        left += 1
        
    return arr
